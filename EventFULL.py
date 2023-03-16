def welcome():
    print("WELCOME TO EVENTFUL")
    from PIL import Image
    myImage = Image.open("logo.png")
    myImage.show()
    print("   MAKE YOUR CALENDARS EVENT-FULL WITH EVENTFUL  ")
    print("")
    print("EVENTFUL is one of singapore&#39;s leading event management websites")
    print("It is an online platform that not only enables users to search for events and theirdetails but also allows the users to add information and specifics about events organised bythem")
    print("")
    print("Provides the users with information about the event such as the available dates,venue,cost of tickets,its description and other specifics")        
  
welcome()
import datetime
x = datetime.datetime.now()
print(x)
login=input("Type &#39;sign up&#39; if new user.Type &#39;sign in&#39; if registered user")
    if login==&#39;sign up&#39; or login== &#39;Sign up&#39;:
        firstname=input("enter your first name")
        lastname=input("enter your last name")
        birthdate=input("enter your birthdate in the format dd/mm/yyyy")
        email=input("enter your email id")
        x=input("enter &#39;done&#39")
            break
    if login==&#39;sign in&#39; or login== &#39;Sign in&#39;:
        username=input("enter username")
        password=input("enter password")
        Break
d={"First Name":firstname,"Last name":lastname, "Birth Date":birthdate,"Email-id":email}

while True:
    a=input("enter ‘1’ to add information about the events you are organizing. Enter ‘2’ to search for upcoming events and their details. Enter ‘q’ or ’Q’ to exit the website") 
    if a=="q"; or a=="Q":
        break
    if a=="1":
        adding_event=input("enter event you wish to add")
        listevents.append(adding_event)
print(listevents) 

while True:
    entername=input("enter your name:")
    enteremailid=input("enter your emailID:")
    add_dates=eval(input("enter your dates for the event"))
    add_descripiton=input("add any further description of your event")
    add_ticketprice=input(“add your ticket price for the event”)
    key=input("press c to continue and q to quit")
    if key=="q" or key=="Q":
        print("your response has been saved. Your details will be added after verification.
Thank you for using Eventful.")
        break
       
                
    if a=="2":
        print(“Genre of events:”)
        lst=”Dance”, “Music”, “Sports”, “Art”
        t=tuple(lst)
        genre=input(“enter the type of event”)
        if genre=="Dance" or genre=="dance":
    print("the list of dance events are:")
    dance_events=["Ultra Singapore","Atara: For you","Dance Appreciation
Series","Dancing Maidens"]
    print(dance_events)
    print("select a dance event to see the available dates")
    event=input("type the dance event you wish to view")
    if event=="Ultra Singapore":
        dance_details1={"available dates": "29-02-20, 30-04-20","venue":"Marina Bay
Sands Theatre Hall","Ticket Price":"$56","Description":"Ultra Singapore is an outdoor
electronic music festival that debuted in 2015 in Singapore as part of Ultra Music Festival&#39;s
worldwide expansion, which has now spread to twenty countries."}
        print(dance_details1)
        for key in dance_details1:
            print(key,":",dance_details1[key])
    if event=="Atara: For you":
        dance_details2={"available dates": "9-11-20, 17-04-20","venue":"Esplanade by
The Bay","Ticket Price":"90","Description":"In ATARA – For you, who has not yet found the
one, Cologne-based choreographer Reut Shemesh directs her gaze onto the world views
and different perspectives of Jewish Orthdox and secular women and their positions towards

each other.Reut Shemesh grew up in a mixed secular/Orthodox family and investigates the
gender roles and tensions within such family structures. Drawing from a series of interviews
and photographic portraits, a mixed cast of Orthodox and secular dancers perform and
transform re-enactments, religious ceremonies, rituals and conversations into a striking
contemporary work."}
        print(dance_details2)
        for key2 in dance_details2:
             print(key2,":",dance_details2[key2])
    if event=="Dance Appreciation Series":
        dance_details3={"available dates": "02-02-20, 3-09-20","venue":"Singapore Dance
Theatre","Ticket Price":"43","Description":"In collaboration with Singapore Dance Theatre
(SDT), Dance Appreciation Series is a ballet education series for children and young adults.
The programme includes both narration and dance excerpts that will educate and excite
those keen on Western classical ballet and newcomers to the genre."}
        print(dance_details3)
        for key3 in dance_details3:
            print(key3,":",dance_details3[key3]
    if event=="Dancing Maidens":
        dance_details4={"available dates": "8-08-20, 03-05-20","venue":"Bayflow","Ticket
Price":"68","Description":"Welcome the arrival of spring with a group of maidens as they
dance by the river and be mesmerised by their elegant and graceful movements. This
showcase is performed by students from Nanyang Girls’ High School, Singapore Chinese
Girls’ School, St. Margaret’s Secondary School and CHIJ St Nicholas Girls’ School."}
        print(dance_details4)
        for key4 in dance_details4:
            print(key4,":",dance_details4[key4])

  if genre=="Music" or genre=="music":
    print("upcoming music events in singapore are:")
    music_events=["Songkran music festival","Stereofest","Hydeout Music
Festival","Shakti","Harry Potter and the Goblet of Fire-Concert"]
    print(music_events)
    print("select a music event to view further information and details")
    musicchoice=input("enter the name of the event")
    if musicchoice=="Songkran music festival":
        details1={"available dates": "11-04-2020","venue":"Wild Wild Wet@Downtown
East","Ticket price":"$79","Description":"Songkran Music Festival is Singapore’s first Music
Festival held in a water park featuring exhilarating water visual effects.Party-goers will also
experience breath taking lighting and water effects throughout the water music festival!"}
        print("the details of the event are:")
        print("")
        print("the available dates are:",details1["available dates"])
        print("")
        print("the venue of the event is:",details1["venue"])
        print("")
        print("the cost of tickets for the event are:",details1["Ticket price"])
        print("")

        descchoice_music1=input("enter &#39;yes&#39; if you wish to view the description.enter &#39;no&#39;
to move onto the next step")
        if descchoice_music1=="Yes" or descchoice_music1=="yes":
            print("the description of the event is:",details1["Description"])
        if descchoice_music1=="no" or descchoice_music1=="No":
            print("The ticket confirmation and invoice will soon be generated in the
following steps")
         
    if musicchoice=="Stereofest":
        details2={"available dates": "22-04-2020 and 23-04-2020","venue":"Palawan
Green@Siloso Beach Walk","Ticket price":"$88","Description":"Organised by RoseValley,
STEREOFEST houses 20 musical acts from the region, namely Indonesia, Malaysia and
Singapore. Besides the non-stop entertainment, the two-day festival also features a Festival
Village, housing plenty of retail and F&amp;B options for all festival-goers to enjoy."}
        print("the details of the event are:")
        print("")
        print("the available dates are:",details2["available dates"])
        print("")
        print("the venue of the event is:",details2["venue"])
        print("")
        print("the cost of tickets for the event are:",details2["Ticket price"])
        print("")
        descchoice_music2=input("enter &#39;yes&#39; if you wish to view the description.enter &#39;no&#39; to
move onto the next step")
        if descchoice_music2=="Yes" or "yes":
            print("the description of the event is:",details2["Description"])
        if descchoice_music2=="no" or descchoice_music2=="No":
            print("The ticket confirmation and invoice will soon be generated in the following
steps")
       
    if musicchoice=="Hydeout Music Festival":
        details3={"available dates":"10-04-2020,11-04-2020","venue":"The Meadow","Ticket
price":"$65","Description":"Created to be a utopia within the hustle and bustle of city life, a
place to channel our pent-up energy and amplify our senses – Hydeout presents a sanctuary
for music seekers to explore music of all kinds.Introducing the region’s first multi-genre
music festival, Hydeout allures and gathers every tastemaker for the most extraordinary
music revelry.More than just a music festival that promotes a universal passion for music,
Hydeout is a celebration of a multi-elemental music scene that tells a story of free-spirited
adventures. Over two weekends, the festival will feature four days of international and
regional artist showcases from various genres in a re-imagined arena."}
        print("the details of the event are:")
        print("")
        print("the available dates are:",details3["available dates"])
        print("")
        print("the venue of the event is:",details3["venue"])
        print("")
        print("the cost of tickets for the event are:",details3["Ticket price"])
        print("")
        descchoice_music3=input("enter &#39;yes&#39; if you wish to view the description.enter &#39;no&#39; to
move onto the next step")
        if descchoice_music3=="no" or  descchoice_music3=="No":
            print("The ticket information and invoice will soon be generated in the following
steps")
        if descchoice_music3=="Yes" or descchoice_music3=="yes":
           print("the description of the event is:",details3["Description"])

       
    if musicchoice=="Shakti":
        details4={"available dates": "16-01-2020","venue":"The Star Performing Arts
Centre","Ticket price":"$85","Description":"Formed in 1973 by guitarist John McLaughlin and
tabla maestro Zakir Hussain , SHAKTI pioneered a groundbreaking East meets West
collaboration and played a pivotal role in establishing Fusion music. The violinist L.Shankar
and ghatam player T.H. Vikku Vinayakram were part of the original band which toured
several years in its original formation around the world to highly acclaimed praise"}
        print("the details of the event are:")
        print("")
        print("the available dates are:",details4["available dates"])
        print("")
        print("the venue of the event is:",details4["venue"])
        print("")
        print("the cost of tickets for the event are:",details4["Ticket price"])
        print("")
        descchoice_music4=input("enter &#39;yes&#39; if you wish to view the description.enter &#39;no&#39; to
move onto the next step")
        if descchoice_music4=="Yes" or descchoice_music4=="yes":
            print("the description of the event is:",details4["Description"])
        if descchoice_music4=="no" or descchoice_music4=="No":
            print("The ticket information and invoice will soon be generated in the following
steps")
 
    if musicchoice=="Harry Potter and the Goblet of Fire-Concert":
        details5={"available dates":"28-02-2020","venue":"Esplanade-Theatres on the
Bay","Ticket price":"$73","Description":"The Harry Potter Film Concert Series returns to the
Esplanade Theatre in Singapore with Harry Potter and the Goblet of Fire™ in Concert, the
fourth film in the Harry Potter series. On February 28th and 29th, 2020, the Metropolitan
Festival Orchestra will perform this magical score live from Harry Potter and the Goblet of
Fire™ while the entire film plays in high-definition on a 40-foot screen"}
        print("the details of the event are:")
        print("")
        print("the available dates are:",details5["available dates"])
        print("")
        print("the venue of the event is:",details5["venue"])
        print("")
        print("the cost of tickets for the event are:",details5["Ticket price"])
        print("")
        descchoice_music5=input("enter &#39;yes&#39; if you wish to view the description.enter &#39;no&#39; to
move onto the next step")
        if descchoice_music5=="Yes" or descchoice_music5=="yes":
            print("the description of the event is:",details5["Description"])
        elif descchoice_music5=="no" or descchoice_music5== "No":
            print("The ticket information and invoice will soon be generated in the following
steps")      
 if genre=="Sports" or genre=="sports":
   print("the list of upcoming sports events in singapore are:")
   sports_events=["Qualifiers-Singapore Badminton Open 2020","ASEAN Basketball
League:Singapore Slingers vs Heat","HSBC Singapore Sevens","Safari Zoo Run","Surf N
Sweat 2020"]
   print(sports_events)
   print("select a sports event to view further information and details")
   sports_choice=input("Enter the name of the event you wish to view")

   if sports_choice=="Qualifiers-Singapore Badminton Open 2020":
       sportsdetails1={"available dates":"07-04-2020","venue":"Singapore Indoor
Stadium","Ticket price":"$65","Description":"World class shuttlers from around the globe will
battle it out at the Singapore Badminton Open 2020.Qualifying Round is on Tuesday, 7 April
2020, 10AM to 6PM.Preliminary round is on 8th April, 10 AM to 10PM. The finals is on 12th
April, 1PM to 7PM"}
       print("the details of the event are:")
       print("the available dates are:",sportsdetails1["available dates"])
       print("the venue of the event is:",sportsdetails1["venue"])
       print("the cost of the tickets are:",sportsdetails1["Ticket price"])
       descchoice_sports=input("enter &#39;yes&#39; if you wish to view the description. Enter &#39;no&#39; to
move onto the next step")
       if descchoice_sports=="Yes" or descchoice_sports=="yes":
           print("the description of the event is",sportsdetails1["Description"])
       if descchoice_sports=="no" or descchoice_sports=="no":
           print("the invoice will be generated after ticket confirmation in the following steps")
      
   if sports_choice=="ASEAN Basketball League:Singapore Slingers vs Heat":
       sportsdetails2={"available dates":"29-01-2020","venue":"OCBC Arena","Ticket
price":"$55","Description":"watch the Singapore Slingers light up the court at OCBC
Arena.Experience the unbelievable atmosphere &amp; top-class hoop action of a Singapore
Slingers home game. Experience the unbelievable atmosphere &amp; top-class hoop action of a
Singapore Slingers home game!! Singapore Slingers are primed to do battle in the 2019-20
ASEAN Basketball League as they compete against quality professional teams from the
Philippines, Indonesia, Malaysia, Vietnam, Thailand, Taiwan, China &amp; Hong Kong in what’s
set to be one of the most tightly contested ABL seasons ever."}
       print("the details of the event are:")
       print("the available dates are:",sportsdetails2["available dates"])
       print("the venue of the event is:",sportsdetails2["venue"])
       print("the cost of the tickets are:",sportsdetails2["Ticket price"])
       descchoice_sports2=input("enter &#39;yes&#39; if you wish to view the description. Enter &#39;no&#39; to
move to the next step")
       if descchoice_sports2=="Yes" or descchoice_sports2=="yes":
           print("the description of the event is",sportsdetails2["Description"])
       if descchoice_sports2=="no" or descchoice_sports2=="no":
           print("the invoice will be generated after ticket confirmation in the following steps")
          
   if sports_choice=="HSBC Singapore Sevens":
       sportsdetails3={"available dates":"11-04-2020,12-04-2020","venue":"National
Stadium","Ticket price":"$45","Description":"The HSBC Singapore Rugby Sevens brings you
a weekend of world class entertainment. Held at the National Stadium on 11 and 12 April
2020, event-goers will enjoy two days of thrilling action on pitch and non-stop entertainment
off it.Fans will get to enjoy the short,fast form of rugby as 16 nations go head-to-head in their
quest to be crowned champions. Dubbed The Family Sevens for its family-centric format,
ticket holders will also enjoy an extensive line-up of off-pitch entertainment at the two-day
carnival, including a Family FunZone, Splash Party, rugby-themed games, live music and
lots more. Don’t miss the best show in town this April!"}
       print("the details of the event are:")
       print("the available dates are:",sportsdetails3["available dates"])
       print("the venue of the event is:",sportsdetails3["venue"])
       print("the cost of the tickets are:",sportsdetails3["Ticket price"])
       descchoice_sports3=input("enter &#39;yes&#39; if you wish to view the description. Enter &#39;no&#39; to
move to the next step")
       if descchoice_sports3=="Yes" or descchoice_sports3=="yes":
           print("the description of the event is",sportsdetails3["Description"])

       if descchoice_sports3=="no" or descchoice_sports3=="no":
           print("the invoice will be generated after ticket confirmation in the following steps") 
   if sports_choice=="Safari Zoo Run":
       sportsdetails4={"available dates":"29-03-2020","venue":"Singapore Zoo","Ticket
price":"$40","Description":"Take part in the final edition of Safari Zoo Run before Mandai&#39;s
major makeover. Choose from the competitive Safari Zoo challenge, duo dash and junior
dash, or the easy Safari Zoo walk. Then pledge your allegiance to any one of Wildlife
Reserves Singapore’s four park icons: Jurong Bird Park’s Sunny the hornbill, Night Safari’s
Chawang the elephant, River Safari’s Canola the manatee and Singapore Zoo’s Ah Meng
the orangutan, and champion a conservation cause"}
       print("the details of the event are:")
       print("the available dates are:",sportsdetails4["available dates"])
       print("the venue of the event is:",sportsdetails4["venue"])
       print("the cost of the tickets are:",sportsdetails4["Ticket price"])
       descchoice_sports4=input("enter &#39;yes&#39; if you wish to view the description. Enter &#39;no&#39; to
move to the next step")
       if descchoice_sports4=="Yes" or descchoice_sports4=="yes":
           print("the description of the event is",sportsdetails4["Description"])
       if descchoice_sports4=="no" or descchoice_sports4=="no":
           print("the invoice will be generated after ticket confirmation in the following steps")
          
   if sports_choice=="Surf N Sweat 2020":
       sportsdetails5={"available dates":"07-03-2020,08-03-2020","venue":"Nanyang
technological university","Ticket price":"$45","Description":"Surf N Sweat is Singapore&#39;s
largest annual beach sporting event, proudly organised by Nanyang Technological
University Sports Club. &#39;ll be making waves at Palawan Beach, Sentosa, so prepare yourself
for a day of adrenaline pumping and exhilarating activities happening on both sand and
sea!Get groovy on 8th March 2020 as we are doing it retro style for our 25th Anniversary!
Come and join us!"}
       print("the details of the event are:")
       print("the available dates are:",sportsdetails5["available dates"])
       print("the venue of the event is:",sportsdetails5["venue"])
       print("the cost of the tickets are:",sportsdetails5["Ticket price"])
       descchoice_sports5=input("enter &#39;yes&#39; if you wish to view the description. Enter &#39;no&#39; to
move to the next step")
       if descchoice_sports5=="Yes" or descchoice_sports5=="yes":
           print("the description of the event is",sportsdetails5["Description"])
       if descchoice_sports5=="no" or descchoice_sports5=="no":
           print("the invoice will be generated after ticket confirmation in the following steps")
 
                   
    

import json
if genre=="Art" or genre=="art":
   x=input("Type ‘exhibition’ or type ‘competition’ according to your preference")
   if x=="exhibition" or x=="Exhibition":

       print("the list of upcoming art exhibitions in singapore are:")
       exhibitions=["Prospect.4","On the Horizon","A Dangerous Woman","About
Face","DuoX4Odell’s","Jamini Roy"]
       print(exhibitions)
       dic1={"available
dates":"30/01/20,2/02/20,10/02/20,18/02/20,27/02/20,2/03/20,11/03/20,17/03/20,30/03/20",
"Venue":"F1 pit building","Price of adult ticket":"$60","Price of child ticket":"$45"}      
dic2={"available
dates":"29/01/20,3/02/20,13/02/20,22/02/20,28/02/20,4/03/20,18/03/20","Venue":"City
Hall","Price of adult ticket":"$70","Price of child ticket":"$55"}
       dic3={"available
dates":"26/01/20,8/02/20,17/02/20,22/02/20,28/02/20,9/03/20,17/03/20",
"Venue":"Serangoon Nex","Price of adult ticket":"$30","Price of child ticket":"$20"}
       dic4={"available dates":"24/01/20,3/02/20,10/02/20,28/02/20,9/03/20,17/03/20",
"Venue":"Baltimore’s Creative Alliance Main Gallery","Price of adult ticket":"$30","Price of
child ticket":"$20"}
        
       dic5={"available dates":"26/01/20,7/02/20,16/02/20,25/02/20,,9/03/20,30/03/20",
"Venue":"Gotham City","Price of adult ticket":"$50","Price of child ticket":"$40"}
       dic6={"available
dates":"25/01/20,7/02/20,15/02/20,22/02/20,28/02/20,17/03/20,29/03/20", "Venue":"Artwalk
Little India","Price of adult ticket":"$80","Price of child ticket":"$60"}

   details=input("enter ‘yes’ in order to view description of events")
   if details=="yes" or details=="Yes":
       event=input("enter the name of the event you wish to see a description of")
       if event=="Prospect.4":
           print("The fourth iteration of this city-wide exhibition includes the works of 73 artists,
who are based primarily in the US, Caribbean, Latin America, and Europe. Organized by
curator Trevor Schoomaker, Prospect 4, includes everything from art and jazz museums to
an antique store and billboards, and is accompanied by over a 100 satellite exhibitions.")
       if event=="On the Horizon":
           print("Internal Landscapes, the first iteration in the multipart On the Horizon, focuses
on a fraught motif in the Cuban historical and aesthetic cosmology, the​​ horizon, and
specifically how it relates to the body. The curation is intelligently expansive; the show
encompasses the many registers of diaspora and exile that frame the Cuban experience,
with works on view by artists born in Miami, artists born on the island and living there like
Yoan Capote, those based elsewhere like New York, and canonical Cuban-born, Miami-
based giants like José Bedia and Gory.")
       if event=="A Dangerous Woman":
           print("A Dangerous Woman: at the Columbus Museum of Art (CMA) is the first survey
since the mid-20th century of the artist’s works, many of which are on loan from her estate,
and showcases a largely uncelebrated powerhouse of multiple styles, including Rockwell-
esque depictions of quotidian American life and unsettling, decidedly feminine Surrealist
portraiture. Credit is due to CMA for putting together a remarkable exhibition on a fascinating
artist worthy of deeper consideration.")
       if event=="About Face":
           print("The group exhibition, About Face, at Baltimore’s Creative Alliance Main Gallery
featured four artists of color who, like Sherald, depict empowered black subjects that exude
a palpable sense of agency. The show featured Rozeal’s Japanese-inspired graphic scrolls,
Tim Okamura’s painterly realism, and Ebony G. Patterson’s baroque fiber-based wall

installations celebrating Jamaican dance culture. With Sherald’s romantic figures at the
center, About Face explored portraiture as an effective tool for envisioning a more inclusive
and authentic America, one created by diverse authors and devoid of tokenism and
exoticism. Together these portraits pointed toward a future art historical cannon where black
faces and figures are the rule, rather than the exception.")
       if event=="DuoX4Odell’s":
           print("Daniel Wickerham and Malcolm Lomax, also known collaboratively as DUOX,
have been making theatrical, multi-media installations that use digital collage, animation,
interactive video, and web design to posit queer-centered narratives since 2009. For
Singapore’s second iteration of Light City, a citywide art and technology festival, the duo was
selected to explore Odell’s, a historic dance club that existed from 1976 to ’92 on North
Avenue and served as an exclusive cultural hub for the African American community.")
       if event=="Jamini Roy":
           print("Jamini Roy (11 April 1887 – 24 April 1972) was an Indian painter. He was
honoured with the State award of Padma Bhushan in 1954. He was one of the most famous
pupils of Rabindranath Tagore, whose artistic originality and contribution to the emergence
of modern art in India remains unquestionable.")
   if details=="no":
       facts=input("enter the event for show details")
       if facts=="Prospect.4":
           print(json.dumps(dic1,indent=2))
       elif facts=="On the Horizon":
           print(json.dumps(dic2,indent=2))
       elif facts=="A Dangerous Woman":
           print(json.dumps(dic3,indent=2))
       elif facts=="About Face":
           print(json.dumps(dic4,indent=2))
       elif facts=="DuoX4Odell&#39;s":
           print(json.dumps(dic5,indent=2))
       elif facts=="Jamini Roy":
           print(json.dumps(dic6,indent=2))
if x=="competition" or "Competition":
        print("the list of upcoming art competitions in singapore are:")
        competitions=["Artshub","GIIS Art","RWCC","SOTA","UOB Painting of the Year"]
        print(competitions)
        dicc1={"Date":"10/02/20", "Venue":"SINDA,Little India","Entry fees for Juniors(5-
10yrs)":"$20-solo,$15-group","Entry fees for Senior(11-17yrs)":"$30-solo,$20-
group","Categories":"Classical, Folk, Fusion"}
        dicc2=dict(zip(("Date","Venue","Entry fees for Junior(8-12yrs)","Entry fees for
Senior(13-19yrs)","Categories"),("15/05/20","Esplanade","$30-solo,$30-group","$30-
solo,$30-group","Classical, Folk, Contemporary")))
        dicc3=dict((("Date","18/02/20"), ("Venue","Edgefield primary School"),("Entry fees for
Junior(5-10yrs)","$30-solo,$35-group"),("Entry fees for Senior(11-19yrs)","$40-solo,$35-
group"),("Categories","Semi-Classical, Folk, Fusion")))
        dicc4=dict((["Date","11/06/20"], ["Venue","Global Indian International School"],["Entry
fees for Junior(9-15yrs)","$10-solo,$15-group"],["Entry fees for Senior(16-24yrs)","$20-
solo,$15-group"],["Categories","Semi-Classical, International folk, Fusion"]))
        dicc5={"Date":"30/07/20", "Venue":"Yishun JC","Entry fees for Junior(7-13yrs)":"$20-
solo,$25-group","Entry fees for Senior(14-20yrs)":"$30-solo,$20-
group","Categories":"Classical, Folk, Hip-hop"}
        artdetail1=input("enter the event you wish to view the details of")
        if artdetail1=="Artshub":
              print("Artshub initiate to create an interactive platform to promote the finest artwork
of all well-known artists, in order to gain the recognition they deserve.  Arts Hub Singapore is

to promote art and artists to an international platform. Their aim is to promote arts activities
that inspire young people with a lasting enthusiasm for the arts, art awareness of our arts
heritage and its conservation and to expand the horizons of young people through their
involvement in creative arts.")
              print("Date of event:",dicc1["Date"])
              print("Venue:",dicc1["Venue"])
              print("Categories:",dicc1["Categories"])
              print("Entry fees for Juniors:",dicc1["Entry fees for Juniors(5-10yrs)"])
              print("Entry fees for Seniors:",dicc1["Entry fees for Senior(11-17yrs)"])
        if artdetail1=="GIIS Art":
              print("GIIS promotes budding artists and inspires them to think out of the box and
bring out their best.")
              print("Date of event:",dicc2["Date"])
              print("Venue:",dicc2["Venue"])
              print("Categories:",dicc2["Categories"])
              print("Entry fees for Juniors:",dicc2["Entry fees for Junior(8-12yrs)"])
              print("Entry fees for Seniors:",dicc2["Entry fees for Senior(13-19yrs)"])
        if artdetail1=="RWCC":
              print("Real World Challenges Conventions is an extraordinary platform that
challenges the ability of students to think .")
              print("Date of event:",dicc3["Date"])
              print("Venue:",dicc3["Venue"])
              print("Categories:",dicc3["Categories"])
              print("Entry fees for Juniors:",dicc3["Entry fees for Junior(5-10yrs)"])
              print("Entry fees for Seniors:",dicc3["Entry fees for Senior(11-19yrs)"])
        if artdetail1=="SOTA" :
              print("SOTA is pleased to announce the third edition of its annual nation-wide
drawing and painting competition. This year, the SOTA Primary 6 Art Competition is proudly
supported by Mapletree.")
              print("Date of event:",dicc4["Date"])
              print("Venue:",dicc4["Venue"])
              print("Categories:",dicc4["Categories"])
              print("Entry fees for Juniors:",dicc4["Entry fees for Junior(9-15yrs)"])
              print("Entry fees for Seniors:",dicc4["Entry fees for Senior(16-24yrs)"])
        if artdetail1=="UOB Painting of the Year" :
              print("Driven by a passion to encourage talented artists in their creative pursuits,
United Overseas Bank (UOB) started the Painting of the Year competition in Singapore in
1982. Today, the annual art competition is the longest-running in Singapore and one of the
most prestigious in Southeast Asia")
              print("Date of event:",dicc5["Date"])
              print("Venue:",dicc5["Venue"])
              print("Categories:",dicc5["Categories"])
              print("Entry fees for Juniors:",dicc5["Entry fees for Junior(7-13yrs)"])
              print("Entry fees for Seniors:",dicc5["Entry fees for Senior(14-20yrs)"])
              print("We invite pupils (who will be in Primary 6 in 2020) who are creative and
budding artists to participate in this visual arts competition.")

listofevents=[‘Dance’,’Music’,’Sports’,’Artexhibitions’,’Artcompetitions’]
dance_events=[&#39;Ultra Singapore&#39;,&#39;Atara: For you&#39;,&#39;Dance Appreciation Series&#39;, &#39;Dancing
Maidens&#39;]
music_events=[&#39;Songkran music festival&#39;,&#39;Stereofest&#39;,&#39;Hydeout Music Festival&#39;,&#39;Shakti&#39;,&#39;Harry
Potter and the Goblet of Fire-Concert&#39;]

sports_events=[&#39;Qualifiers-Singapore Badminton Open 2020&#39;,&#39;ASEAN Basketball League:
Singapore Slingers vs Heat&#39;,&#39;HSBC Singapore Sevens&#39;,&#39;Safari Zoo Run&#39;,&#39;Surf N Sweat 2020&#39;]
art_events=["Prospect.4","On the Horizon","A Dangerous Woman","About
Face","DuoX4Odell’s","Jamini Roy"]
arts_events=["Artshub","GIIS Art","RWCC","SOTA","UOB Painting of the Year"]

a=input("enter the genre of event you want to choose")
booking_fee=60
print("the booking fee for the events is",booking_fee)
ticketprice_dance1=56
ticketprice_dance2=90
ticketprice_dance3=43
ticketprice_dance4=68
ticketprice_music1=79
ticketprice_music2=88
ticketprice_music3=65
ticketprice_music4=85
ticketprice_music5=73
ticketprice_sports1=65
ticketprice_sports2=55
ticketprice_sports3=45
ticketprice_sports4=40
ticketprice_sports5=45
ticketprice_childart1=45
ticketprice_adultart1=60
ticketprice_childart2=55
ticketprice_adultart2=79
ticketprice_childart3=20
ticketprice_adultart3=30
ticketprice_childart4=20
ticketprice_adultart4=30
ticketprice_childart5=40
ticketprice_adultart5=50
ticketprice_childart6=60
ticketprice_adultart6=80
ticketprice_juniorsolo1=20
ticketprice_juniorgroup1=15
ticketprice_seniorsolo1=30
ticketprice_seniorgroup1=20
ticketprice_juniorsolo2=30
ticketprice_juniorgroup2=30
ticketprice_seniorsolo2=30
ticketprice_seniorgroup2=30
ticketprice_juniorsolo3=30
ticketprice_juniorgroup3=35
ticketprice_seniorsolo3=40
ticketprice_seniorgroup3=35
ticketprice_juniorsolo4=10

ticketprice_juniorgroup4=15
ticketprice_seniorsolo4=20
ticketprice_seniorgroup4=15
ticketprice_juniorsolo5=20
ticketprice_juniorgroup5=25
ticketprice_seniorsolo5=30
ticketprice_seniorgroup5=20

def my_dancefunction():
    ticketprice=0
    print("enter the dance event from the following",dance_events)
    select_dance=input("enter the dance event you wish to select")
    print(select_dance)
    if select_dance==&#39;Ultra Singapore&#39;:
        print("the total charge is:" ,ticketprice_dance1+booking_fee)
        ticketprice+=1
    if select_dance==&#39;Atara: For you&#39;:
        print("the total charge is:" ,ticketprice_dance2+booking_fee)
        ticketprice+=1
    if select_dance==&#39;Dance Appreciation 
Series&#39;:
        print("the total charge is:" ,ticketprice_dance3+booking_fee)
        ticketprice+=1
    if select_dance==&#39;Dancing Maidens&#39;:
        print("the total charge is:" ,ticketprice_dance4+booking_fee)
        ticketprice+=1
        

def my_musicfunction():
    ticketprice=0
    print("enter the music event from the following",music_events)
    select_music=input("enter the music event you wish to select")
    print(select_music)
    if select_music==&#39;Songkran music festival&#39;:
        print("the total charge is:" ,ticketprice_music1+booking_fee)
    if select_music==&#39;Stereofest&#39;:
        print("the total charge is:" ,ticketprice_music2+booking_fee)
    if select_music==&#39;Hydeout Music Festival&#39;:
        print("the total charge is:" ,ticketprice_music3+booking_fee)
    if select_music==&#39;Shakti&#39;:
        print("the total charge is:" ,ticketprice_music4+booking_fee)
    if select_music==&#39;Harry Potter and the Goblet of Fire-Concert&#39;:
        print("the total charge is:" ,ticketprice_music5+booking_fee)

def my_sportsfunction():
    print("enter the sports event from the following",sports_events)
    select_sports=input("enter the sports event you wish to select")
    print(select_sports)
    if select_sports==&#39;Qualifiers-Singapore Badminton Open 2020&#39;:
        print("the total charge is:" ,ticketprice_sports1+booking_fee)
    if select_sports==&#39;ASEAN Basketball League: Singapore Slingers vs Heat&#39;:
        print("the total charge is:" ,ticketprice_sports2+booking_fee)
    if select_sports==&#39;HSBC Singapore Sevens&#39;:
        print("the total charge is:" ,ticketprice_sports3+booking_fee)
    if select_sports==&#39;Safari Zoo Run&#39;:
        print("the total charge is:" ,ticketprice_sports4+booking_fee)
    if select_sports==&#39;Surf N Sweat 2020&#39;:
        print("the total charge is:" ,ticketprice_sports5+booking_fee)
def my_artfunction():
    print("enter the art event from the following",art_events)
    select_art=input("enter the art event you wish to select")
    print(select_art)
    if select_art==&#39;Prospect.4&#39;:
        print("the total charge for child is:" ,ticketprice_childart1+booking_fee)
        print("the total charge for adult is:" ,ticketprice_adultart1+booking_fee)
        
    if select_art==&#39;On the Horizon&#39;:
        print("the total charge for child is:" ,ticketprice_childart2+booking_fee)
        print("the total charge for adult is:" ,ticketprice_adultart2+booking_fee)
        
    if select_art==&#39;A Dangerous Woman&#39;:
        print("the total charge for child is:" ,ticketprice_childart3+booking_fee)
        print("the total charge for adult is:" ,ticketprice_adultart3+booking_fee)
        
    if select_art==&#39;About Face&#39;:
        print("the total charge for child is:" ,ticketprice_childart4+booking_fee)
        print("the total charge for adult is:" ,ticketprice_adultart4+booking_fee)
       
    if select_art==&#39;DuoX4Odell’s&#39;:
        print("the total charge for child is:" ,ticketprice_childart5+booking_fee)
        print("the total charge for adult is:" ,ticketprice_adultart5+booking_fee)
        
    if select_art==&#39;Jamini Roy&#39;:
       print("the total charge for child is:" ,ticketprice_childart6+booking_fee)
       print("the total charge for adult is:" ,ticketprice_adultart6+booking_fee)
        
def my_artsfunction():
    print("enter the art event from the following",arts_events)
    select_arts=input("enter the dance event you wish to select")
    print(select_arts)
    if select_arts==&#39;ArtsHub&#39;:
        print("the total charge for junior solo is:" ,ticketprice_juniorsolo1+booking_fee)
        print("the total charge for junios group is:" ,ticketprice_juniorgroup1+booking_fee)
        print("the total charge for senior solo is:" ,ticketprice_seniorsolo1+booking_fee)
        print("the total charge for senior group is:" ,ticketprice_seniorgroup1+booking_fee)
        ticketprice+=1
    if select_arts==&#39;GIIS Art&#39;:

        print("the total charge for junior solo is:" ,ticketprice_juniorsolo2+booking_fee)
        print("the total charge for junior group is:" ,ticketprice_juniorgroup2+booking_fee)
        print("the total charge for senior solo is:" ,ticketprice_seniorsolo2+booking_fee)
        print("the total charge for senior group is:" ,ticketprice_seniorgroup2+booking_fee)
        ticketprice+=1
    if select_arts==&#39;RWCC&#39;:
        print("the total charge for junior solo is:" ,ticketprice_juniorsolo3+booking_fee)
        print("the total charge for junior group is:" ,ticketprice_juniorgroup3+booking_fee)
        print("the total charge for senior solo is:" ,ticketprice_seniorsolo3+booking_fee)
        print("the total charge for senior group is:" ,ticketprice_seniorgroup3+booking_fee)
        ticketprice+=1
    if select_arts==&#39;SOTA&#39;:
        print("the total charge for junior solo is:" ,ticketprice_juniorsolo4+booking_fee)
        print("the total charge for junior group is:" ,ticketprice_juniorgroup4+booking_fee)
        print("the total charge for senior solo is:" ,ticketprice_seniorsolo4+booking_fee)
        print("the total charge for senior group is:" ,ticketprice_seniorgroup4+booking_fee)
        ticketprice+=1
        
    if select_arts==&#39;UOB Painting of the Year&#39;:
        print("the total charge for junior solo is:" ,ticketprice_juniorsolo5+booking_fee)
        print("the total charge for junior group is:" ,ticketprice_juniorgroup5+booking_fee)
        print("the total charge for senior solo is:" ,ticketprice_seniorsolo5+booking_fee)
        print("the total charge for senior group is:" ,ticketprice_seniorgroup5+booking_fee)
        ticketprice+=1

    
for i in listofevents:
    if i==a:
        print("the event you have chosen is",i)
        print(a)
if a==&#39;dance&#39; or a==&#39;Dance&#39;:
    my_dancefunction()
if a==&#39;music&#39; or a== &#39;Music&#39;:
    my_musicfunction()
if a==&#39;sports&#39; or a==&#39;Sports&#39;:
    my_sportsfunction()
if a==&#39;artexhibitons’ or a==&#39;Artexhibitions&#39;:
    my_artfunction()
If a==’artcompetitions’ or a==‘Artcompetitions’:
    my_artsfunction()

def thankyou():
    print("Thank You for using EVENTFUL”)
    n=input("enter yes for feedback")
    if n=="yes":

        x=input("enter feedback")
        print("Thank you for your feedback")
        print("ticket info")
    else:
        print("ticket info")
thankyou()
