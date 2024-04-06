import streamlit as st
import pandas as pd
import numpy as np
import pickle

from utils import find_postal
from utils import find_nearest

with open('randomforest.pkl', 'rb') as f:
    models_data = pickle.load(f)

models = models_data['models']
feature_names = models_data['feature_names']

@st.cache_data()
def load_data(filepath):
    return pd.read_csv(filepath)
    
def predict_price(features, feature_names):
    model_rf = models['RandomForestRegressor']['model']

    X_df = pd.DataFrame([features], columns=feature_names)

    prediction_rf = model_rf.predict(X_df)

    st.write(f"Predicted Price: ${prediction_rf[0]:.2f}")



shoppingMall_coordinates = load_data('coordinates_data/shopping_mall_coordinates.csv')
mrt_coordinates = load_data('coordinates_data/mrt_coordinates.csv')[['STN_NAME','Latitude','Longitude']]
school_coordinates = load_data('coordinates_data/school_coordinates.csv')[['Name','LATITUDE','LONGITUDE']]
hawker_coordinates = load_data('coordinates_data/hdb_hawker_coordinates.csv')[['address','LATITUDE','LONGITUDE']]

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
storey = st.slider('Maximum Storey', 3,51,12)
year = st.text_input("Current Year", '2017') 
lease_commence_date = st.slider('Lease Commencement Date',1966,2017,1979)
predict_button = st.button("Predict Price")


coord = find_postal(flat_address)
try:
 
    flat_coord = pd.read_csv('final_merged_dataset.csv')
    

    flat_coord = pd.DataFrame({'address':[coord.get('results')[0].get('ADDRESS')],
                            'LATITUDE':[coord.get('results')[0].get('LATITUDE')], 
                        'LONGITUDE':[coord.get('results')[0].get('LONGITUDE')],
                        'POSTAL' : [coord.get('results')[0].get('POSTAL')]
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

nearest_school,school_1km = find_nearest(flat_coord, school_coordinates)
flat_school = pd.DataFrame.from_dict(nearest_school).T
flat_school = flat_school.rename(columns={0: 'flat', 1: 'school', 2: 'school_dist',
                                    3: 'school_within_1km'}).reset_index().drop('index', axis=1)
school_1km['type'] = ['School']*len(school_1km)

nearest_hawker,hawker_1km = find_nearest(flat_coord, hawker_coordinates)
flat_hawker = pd.DataFrame.from_dict(nearest_hawker).T
flat_hawker = flat_hawker.rename(columns={0: 'flat', 1: 'hawker', 2: 'hawker_dist',
                                    3: 'hawker_within_1km'}).reset_index().drop('index', axis=1)
hawker_1km['type'] = ['Hawker']*len(hawker_1km)



show_amenities_button = st.button("Show Nearest Amenities")

if show_amenities_button:
    st.subheader("Nearest Amenities")
    st.text("\n") 

    if flat_mrt.empty:
        st.write("No MRT station found nearby.")
    else:
        mrt_distance = "Within 1 km" if flat_mrt['mrt_within_1km'].iloc[0] else "More than 1 km"
        nearest_mrt_name = flat_mrt['mrt'].iloc[0]
        st.write(f"MRT Station: {nearest_mrt_name.title()} ({mrt_distance})")

    if flat_mall.empty:
        st.write("No shopping mall found nearby.")
    else:
        mall_distance = "Within 1 km" if flat_mall['mall_within_1km'].iloc[0] else "More than 1 km"
        st.write(f"Shopping Mall: {flat_mall['mall'].iloc[0]} ({mall_distance})")

    if flat_mrt.empty:
        st.write("No Primary School found nearby.")
    else:
        school_distance = "Within 1 km" if flat_school['school_within_1km'].iloc[0] else "More than 1 km"
        st.write(f"Nearest Primary School: {flat_school['school'].iloc[0]} ({school_distance})")

    if flat_mrt.empty:
        st.write("No Hawker Centre found nearby.")
    else:
        hawker_distance = "Within 1 km" if flat_hawker['hawker_within_1km'].iloc[0] else "More than 1 km"
        st.write(f"Hawker Centre: {flat_hawker['hawker'].iloc[0]} ({hawker_distance})")

features = {}
print("\n")
print("Features")
features['FloorAreaSqm'] = floor_area
print("Floor area: " + str(floor_area) )

features['LeaseCommenceDate'] = lease_commence_date
print("Lease commence date: " + str(lease_commence_date) )

features['EndStoreyRange'] = storey
print("End Storey Range: " + str(storey) )

features['Year'] = int(year)
print("Year: " + str(year) )

features['Latitude'] = flat_coord['LATITUDE'].iloc[0] 
print("Latitude: " + str(flat_coord['LATITUDE'].iloc[0] ) )

features['Longitude'] = flat_coord['LONGITUDE'].iloc[0] 
print("Longitude: " + str(flat_coord['LONGITUDE'].iloc[0] ) )


features['Postal'] = flat_coord['POSTAL'].iloc[0] 
print("Postal: " + str(flat_coord['POSTAL'].iloc[0] ) )


features['DistanceFromShoppingMall'] = flat_mall['mall_dist'].iloc[0]
print("DistanceFromShoppingMall: " + str(flat_mall['mall_dist'].iloc[0] ) )

features['DistanceFromMRT'] = flat_mrt['mrt_dist'].iloc[0]
print("DistanceDistanceFromMRTFromShoppingMall: " + str(flat_mrt['mrt_dist'].iloc[0] ) )

features['DistanceFromSchool'] = flat_school['school_dist'].iloc[0]
print("DistanceFromSchool: " + str(flat_school['school_dist'].iloc[0] ) )

features['DistanceFromHawkerCentre'] = flat_hawker['hawker_dist'].iloc[0]
print("DistanceFromHawkerCentre: " + str(flat_hawker['hawker_dist'].iloc[0] ) )



for town_cat in town_categories:
    features[f'Town_{town_cat}'] = 1 if town == town_cat else 0


for flat_type_cat in flat_type_categories:
    features[f'FlatType_{flat_type_cat}'] = 1 if flat_type == flat_type_cat else 0


for flat_model_cat in flat_model_categories:
    features[f'FlatModel_{flat_model_cat}'] = 1 if flat_model == flat_model_cat else 0

if predict_button:
    predict_price(features,feature_names)
    
