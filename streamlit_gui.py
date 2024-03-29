import streamlit as st
import pandas as pd
import numpy as np
import pickle


from utils_draft import find_postal
from utils_draft import find_nearest


with open('regression_models_guisl.pkl', 'rb') as f:
    models = pickle.load(f)


@st.cache_data()
def load_data(filepath):
    return pd.read_csv(filepath)

def predict_price(features):
    prediction_gb = models['HistGradientBoostingRegressor'].predict([list(features.values())])[0]
    prediction_dt = models['DecisionTreeRegressor'].predict([list(features.values())])[0]
    prediction_rf = models['RandomForestRegressor'].predict([list(features.values())])[0]
    
    st.write("Predicted Prices:")
    st.write(f"Gradient Boosting Regressor Prediction: ${prediction_gb:.2f}")
    st.write(f"Decision Tree Regressor Prediction: ${prediction_dt:.2f}")
    st.write(f"Random Forest Regressor Prediction: ${prediction_rf:.2f}")




shoppingMall_coordinates = load_data('coordinates_data/shopping_mall_coordinates.csv')
mrt_coordinates = load_data('coordinates_data/mrt_coordinates.csv')[['STN_NAME','Latitude','Longitude']]

town_categories = ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
                   'BUKIT PANJANG', 'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG',
                   'CLEMENTI', 'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
                   'KALLANG/WHAMPOA', 'MARINE PARADE', 'PASIR RIS', 'PUNGGOL',
                   'QUEENSTOWN', 'SEMBAWANG', 'SENGKANG', 'SERANGOON', 'TAMPINES',
                   'TOA PAYOH', 'WOODLANDS', 'YISHUN']

flat_type_categories = ['2 ROOM', '3 ROOM', '4 ROOM', '5 ROOM', 'EXECUTIVE']

flat_model_categories = ['2-room', 'Adjoined flat', 'Apartment', 'DBSS', 'Improved',
                         'Improved-Maisonette', 'Maisonette', 'Model A', 'Model A-Maisonette',
                         'Model A2', 'New Generation', 'Premium Apartment', 'Premium Apartment Loft',
                         'Premium Maisonette', 'Simplified', 'Standard', 'Terrace', 'Type S1', 'Type S2']


flat_address = st.text_input("Flat Address or Postal Code", '406 ANG MO KIO AVE 10') # flat address
town = st.selectbox('Town', town_categories, index=0)
flat_model = st.selectbox('Flat Model', flat_model_categories, index=4)
flat_type = st.selectbox('Flat Type', flat_type_categories, index=0)
floor_area = st.slider("Floor Area (sqm)", 34, 280, 44)
# storey = st.selectbox('Maximum Storey', list(map(str, range(3, 51))), index=2)
storey = st.slider('Maximum Storey', 3,51,12)
year = st.text_input("Current Year", '2017') 
# lease_commence_date = st.selectbox('Lease Commencement Date', list(reversed(range(1966, 2017))), index=1)
lease_commence_date = st.slider('Lease Commencement Date',1966,2017,1979)


coord = find_postal(flat_address)
try:
 
    flat_coord = pd.read_csv('final_merged_dataset.csv')
    

    flat_coord = pd.DataFrame({'address':[coord.get('results')[0].get('ADDRESS')],
                            'LATITUDE':[coord.get('results')[0].get('LATITUDE')], 
                        'LONGITUDE':[coord.get('results')[0].get('LONGITUDE')],
                        # 'POSTAL' : [coord.get('results')[0].get('POSTAL')]
                        })
    
except IndexError:
    st.error('Oops! Address is not valid! Please enter a valid address!')


nearest_mall,malls_1km = find_nearest(flat_coord, shoppingMall_coordinates)
flat_mall = pd.DataFrame.from_dict(nearest_mall).T
flat_mall = flat_mall.rename(columns={0: 'flat', 1: 'mall', 2: 'mall_dist',
                                      3: 'mall_within_1km'}).reset_index().drop('index', axis=1)
malls_1km['type'] = ['Mall']*len(malls_1km)


nearest_mrt,mrt_1km = find_nearest(flat_coord, mrt_coordinates)
flat_mrt = pd.DataFrame.from_dict(nearest_mrt).T
flat_mrt = flat_mrt.rename(columns={0: 'flat', 1: 'mrt', 2: 'mrt_dist',
                                    3: 'mrt_within_1km'}).reset_index().drop('index', axis=1)
mrt_1km['type'] = ['MRT']*len(mrt_1km)


st.subheader("Nearest MRT")
if flat_mrt.empty:
    st.write("No MRT station found nearby.")
else:
    st.write(f"Nearest MRT Station: {flat_mrt['mrt'].iloc[0]}")
    st.write(f"Distance to MRT Station: {flat_mrt['mrt_dist'].iloc[0]} meters")

st.subheader("Nearest Shopping Mall")
if flat_mall.empty:
    st.write("No shopping mall found nearby.")
else:
    st.write(f"Nearest Shopping Mall: {flat_mall['mall'].iloc[0]}")
    st.write(f"Distance to Shopping Mall: {flat_mall['mall_dist'].iloc[0]} meters")


features = {}
features['FloorAreaSqm'] = floor_area
features['LeaseCommenceDate'] = lease_commence_date
features['EndStoreyRange'] = storey
features['Year'] = int(year)
features['Latitude'] = flat_coord['LATITUDE'].iloc[0]  
features['Longitude'] = flat_coord['LONGITUDE'].iloc[0] 
# features['Postal'] = flat_coord['Postal'].iloc[0] s

features['DistanceFromShoppingMall'] = flat_mall['mall_dist'].iloc[0]
features['DistanceFromMRT'] = flat_mrt['mrt_dist'].iloc[0]


for town_cat in town_categories:
    features[f'Town_{town_cat}'] = 1 if town == town_cat else 0


for flat_type_cat in flat_type_categories:
    features[f'FlatType_{flat_type_cat}'] = 1 if flat_type == flat_type_cat else 0


for flat_model_cat in flat_model_categories:
    features[f'FlatModel_{flat_model_cat}'] = 1 if flat_model == flat_model_cat else 0


predict_button = st.button("Predict Price")
if predict_button:
    predict_price(features)

