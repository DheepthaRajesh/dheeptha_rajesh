def welcome():
    print(&quot;WELCOME TO EVENTFUL&quot;)
    from PIL import Image
    myImage = Image.open(&quot;logo.png&quot;)
    myImage.show()
    print(&quot;   MAKE YOUR CALENDARS EVENT-FULL WITH EVENTFUL  &quot;)
    print(&quot;&quot;)
    print(&quot;EVENTFUL is one of singapore&#39;s leading event management websites&quot;)
    print(&quot;It is an online platform that not only enables users to search for events and their
details but also allows the users to add information and specifics about events organised by
them&quot;)
    print(&quot;&quot;)
    print(&quot;Provides the users with information about the event such as the available
dates,venue,cost of tickets,its description and other specifics&quot;)        
  
welcome()
import datetime
x = datetime.datetime.now()
print(x)
login=input(&quot;Type &#39;sign up&#39; if new user.Type &#39;sign in&#39; if registered user&quot;)
    if login==&#39;sign up&#39; or login== &#39;Sign up&#39;:
        firstname=input(&quot;enter your first name&quot;)
        lastname=input(&quot;enter your last name&quot;)
        birthdate=input(&quot;enter your birthdate in the format dd/mm/yyyy&quot;)
        email=input(&quot;enter your email id&quot;)
        x=input(&quot;enter &#39;done&#39;&quot;)
            break
    if login==&#39;sign in&#39; or login== &#39;Sign in&#39;:
        username=input(&quot;enter username&quot;)
        password=input(&quot;enter password&quot;)
        Break
d={&quot;First Name&quot;:firstname,&quot;Last name&quot;:lastname, &quot;Birth Date&quot;:birthdate,&quot;Email-id&quot;:email}

while True:
    a=input(&quot;enter ‘1’ to add information about the events you are organizing. Enter ‘2’ to
search for upcoming events and their details. Enter ‘q’ or ’Q’ to exit the website&quot;) 
    if a==&quot;q&quot; or a==&quot;Q&quot;:
        break
    if a==&quot;1&quot;:
        adding_event=input(&quot;enter event you wish to add&quot;)
        listevents.append(adding_event)
print(listevents) 

while True:
    entername=input(&quot;enter your name:&quot;)
    enteremailid=input(&quot;enter your emailID:&quot;)
    add_dates=eval(input(&quot;enter your dates for the event&quot;))
    add_descripiton=input(&quot;add any further description of your event&quot;)
    add_ticketprice=input(“add your ticket price for the event”)
    key=input(&quot;press c to continue and q to quit&quot;)
    if key==&quot;q&quot; or key==&quot;Q&quot;:
        print(&quot;your response has been saved. Your details will be added after verification.
Thank you for using Eventful.&quot;)
        break
       
                
    if a==&quot;2&quot;:
        print(“Genre of events:”)
        lst=”Dance”, “Music”, “Sports”, “Art”
        t=tuple(lst)
        genre=input(“enter the type of event”)
        if genre==&quot;Dance&quot; or genre==&quot;dance&quot;:
    print(&quot;the list of dance events are:&quot;)
    dance_events=[&quot;Ultra Singapore&quot;,&quot;Atara: For you&quot;,&quot;Dance Appreciation
Series&quot;,&quot;Dancing Maidens&quot;]
    print(dance_events)
    print(&quot;select a dance event to see the available dates&quot;)
    event=input(&quot;type the dance event you wish to view&quot;)
    if event==&quot;Ultra Singapore&quot;:
        dance_details1={&quot;available dates&quot;: &quot;29-02-20, 30-04-20&quot;,&quot;venue&quot;:&quot;Marina Bay
Sands Theatre Hall&quot;,&quot;Ticket Price&quot;:&quot;$56&quot;,&quot;Description&quot;:&quot;Ultra Singapore is an outdoor
electronic music festival that debuted in 2015 in Singapore as part of Ultra Music Festival&#39;s
worldwide expansion, which has now spread to twenty countries.&quot;}
        print(dance_details1)
        for key in dance_details1:
            print(key,&quot;:&quot;,dance_details1[key])
    if event==&quot;Atara: For you&quot;:
        dance_details2={&quot;available dates&quot;: &quot;9-11-20, 17-04-20&quot;,&quot;venue&quot;:&quot;Esplanade by
The Bay&quot;,&quot;Ticket Price&quot;:&quot;90&quot;,&quot;Description&quot;:&quot;In ATARA – For you, who has not yet found the
one, Cologne-based choreographer Reut Shemesh directs her gaze onto the world views
and different perspectives of Jewish Orthdox and secular women and their positions towards

each other.Reut Shemesh grew up in a mixed secular/Orthodox family and investigates the
gender roles and tensions within such family structures. Drawing from a series of interviews
and photographic portraits, a mixed cast of Orthodox and secular dancers perform and
transform re-enactments, religious ceremonies, rituals and conversations into a striking
contemporary work.&quot;}
        print(dance_details2)
        for key2 in dance_details2:
             print(key2,&quot;:&quot;,dance_details2[key2])
    if event==&quot;Dance Appreciation Series&quot;:
        dance_details3={&quot;available dates&quot;: &quot;02-02-20, 3-09-20&quot;,&quot;venue&quot;:&quot;Singapore Dance
Theatre&quot;,&quot;Ticket Price&quot;:&quot;43&quot;,&quot;Description&quot;:&quot;In collaboration with Singapore Dance Theatre
(SDT), Dance Appreciation Series is a ballet education series for children and young adults.
The programme includes both narration and dance excerpts that will educate and excite
those keen on Western classical ballet and newcomers to the genre.&quot;}
        print(dance_details3)
        for key3 in dance_details3:
            print(key3,&quot;:&quot;,dance_details3[key3]
    if event==&quot;Dancing Maidens&quot;:
        dance_details4={&quot;available dates&quot;: &quot;8-08-20, 03-05-20&quot;,&quot;venue&quot;:&quot;Bayflow&quot;,&quot;Ticket
Price&quot;:&quot;68&quot;,&quot;Description&quot;:&quot;Welcome the arrival of spring with a group of maidens as they
dance by the river and be mesmerised by their elegant and graceful movements. This
showcase is performed by students from Nanyang Girls’ High School, Singapore Chinese
Girls’ School, St. Margaret’s Secondary School and CHIJ St Nicholas Girls’ School.&quot;}
        print(dance_details4)
        for key4 in dance_details4:
            print(key4,&quot;:&quot;,dance_details4[key4])

  if genre==&quot;Music&quot; or genre==&quot;music&quot;:
    print(&quot;upcoming music events in singapore are:&quot;)
    music_events=[&quot;Songkran music festival&quot;,&quot;Stereofest&quot;,&quot;Hydeout Music
Festival&quot;,&quot;Shakti&quot;,&quot;Harry Potter and the Goblet of Fire-Concert&quot;]
    print(music_events)
    print(&quot;select a music event to view further information and details&quot;)
    musicchoice=input(&quot;enter the name of the event&quot;)
    if musicchoice==&quot;Songkran music festival&quot;:
        details1={&quot;available dates&quot;: &quot;11-04-2020&quot;,&quot;venue&quot;:&quot;Wild Wild Wet@Downtown
East&quot;,&quot;Ticket price&quot;:&quot;$79&quot;,&quot;Description&quot;:&quot;Songkran Music Festival is Singapore’s first Music
Festival held in a water park featuring exhilarating water visual effects.Party-goers will also
experience breath taking lighting and water effects throughout the water music festival!&quot;}
        print(&quot;the details of the event are:&quot;)
        print(&quot;&quot;)
        print(&quot;the available dates are:&quot;,details1[&quot;available dates&quot;])
        print(&quot;&quot;)
        print(&quot;the venue of the event is:&quot;,details1[&quot;venue&quot;])
        print(&quot;&quot;)
        print(&quot;the cost of tickets for the event are:&quot;,details1[&quot;Ticket price&quot;])
        print(&quot;&quot;)

        descchoice_music1=input(&quot;enter &#39;yes&#39; if you wish to view the description.enter &#39;no&#39;
to move onto the next step&quot;)
        if descchoice_music1==&quot;Yes&quot; or descchoice_music1==&quot;yes&quot;:
            print(&quot;the description of the event is:&quot;,details1[&quot;Description&quot;])
        if descchoice_music1==&quot;no&quot; or descchoice_music1==&quot;No&quot;:
            print(&quot;The ticket confirmation and invoice will soon be generated in the
following steps&quot;)
         
    if musicchoice==&quot;Stereofest&quot;:
        details2={&quot;available dates&quot;: &quot;22-04-2020 and 23-04-2020&quot;,&quot;venue&quot;:&quot;Palawan
Green@Siloso Beach Walk&quot;,&quot;Ticket price&quot;:&quot;$88&quot;,&quot;Description&quot;:&quot;Organised by RoseValley,
STEREOFEST houses 20 musical acts from the region, namely Indonesia, Malaysia and
Singapore. Besides the non-stop entertainment, the two-day festival also features a Festival
Village, housing plenty of retail and F&amp;B options for all festival-goers to enjoy.&quot;}
        print(&quot;the details of the event are:&quot;)
        print(&quot;&quot;)
        print(&quot;the available dates are:&quot;,details2[&quot;available dates&quot;])
        print(&quot;&quot;)
        print(&quot;the venue of the event is:&quot;,details2[&quot;venue&quot;])
        print(&quot;&quot;)
        print(&quot;the cost of tickets for the event are:&quot;,details2[&quot;Ticket price&quot;])
        print(&quot;&quot;)
        descchoice_music2=input(&quot;enter &#39;yes&#39; if you wish to view the description.enter &#39;no&#39; to
move onto the next step&quot;)
        if descchoice_music2==&quot;Yes&quot; or &quot;yes&quot;:
            print(&quot;the description of the event is:&quot;,details2[&quot;Description&quot;])
        if descchoice_music2==&quot;no&quot; or descchoice_music2==&quot;No&quot;:
            print(&quot;The ticket confirmation and invoice will soon be generated in the following
steps&quot;)
       
    if musicchoice==&quot;Hydeout Music Festival&quot;:
        details3={&quot;available dates&quot;:&quot;10-04-2020,11-04-2020&quot;,&quot;venue&quot;:&quot;The Meadow&quot;,&quot;Ticket
price&quot;:&quot;$65&quot;,&quot;Description&quot;:&quot;Created to be a utopia within the hustle and bustle of city life, a
place to channel our pent-up energy and amplify our senses – Hydeout presents a sanctuary
for music seekers to explore music of all kinds.Introducing the region’s first multi-genre
music festival, Hydeout allures and gathers every tastemaker for the most extraordinary
music revelry.More than just a music festival that promotes a universal passion for music,
Hydeout is a celebration of a multi-elemental music scene that tells a story of free-spirited
adventures. Over two weekends, the festival will feature four days of international and
regional artist showcases from various genres in a re-imagined arena.&quot;}
        print(&quot;the details of the event are:&quot;)
        print(&quot;&quot;)
        print(&quot;the available dates are:&quot;,details3[&quot;available dates&quot;])
        print(&quot;&quot;)
        print(&quot;the venue of the event is:&quot;,details3[&quot;venue&quot;])
        print(&quot;&quot;)
        print(&quot;the cost of tickets for the event are:&quot;,details3[&quot;Ticket price&quot;])
        print(&quot;&quot;)
        descchoice_music3=input(&quot;enter &#39;yes&#39; if you wish to view the description.enter &#39;no&#39; to
move onto the next step&quot;)
        if descchoice_music3==&quot;no&quot; or  descchoice_music3==&quot;No&quot;:
            print(&quot;The ticket information and invoice will soon be generated in the following
steps&quot;)
        if descchoice_music3==&quot;Yes&quot; or descchoice_music3==&quot;yes&quot;:
           print(&quot;the description of the event is:&quot;,details3[&quot;Description&quot;])

       
    if musicchoice==&quot;Shakti&quot;:
        details4={&quot;available dates&quot;: &quot;16-01-2020&quot;,&quot;venue&quot;:&quot;The Star Performing Arts
Centre&quot;,&quot;Ticket price&quot;:&quot;$85&quot;,&quot;Description&quot;:&quot;Formed in 1973 by guitarist John McLaughlin and
tabla maestro Zakir Hussain , SHAKTI pioneered a groundbreaking East meets West
collaboration and played a pivotal role in establishing Fusion music. The violinist L.Shankar
and ghatam player T.H. Vikku Vinayakram were part of the original band which toured
several years in its original formation around the world to highly acclaimed praise&quot;}
        print(&quot;the details of the event are:&quot;)
        print(&quot;&quot;)
        print(&quot;the available dates are:&quot;,details4[&quot;available dates&quot;])
        print(&quot;&quot;)
        print(&quot;the venue of the event is:&quot;,details4[&quot;venue&quot;])
        print(&quot;&quot;)
        print(&quot;the cost of tickets for the event are:&quot;,details4[&quot;Ticket price&quot;])
        print(&quot;&quot;)
        descchoice_music4=input(&quot;enter &#39;yes&#39; if you wish to view the description.enter &#39;no&#39; to
move onto the next step&quot;)
        if descchoice_music4==&quot;Yes&quot; or descchoice_music4==&quot;yes&quot;:
            print(&quot;the description of the event is:&quot;,details4[&quot;Description&quot;])
        if descchoice_music4==&quot;no&quot; or descchoice_music4==&quot;No&quot;:
            print(&quot;The ticket information and invoice will soon be generated in the following
steps&quot;)
 
    if musicchoice==&quot;Harry Potter and the Goblet of Fire-Concert&quot;:
        details5={&quot;available dates&quot;:&quot;28-02-2020&quot;,&quot;venue&quot;:&quot;Esplanade-Theatres on the
Bay&quot;,&quot;Ticket price&quot;:&quot;$73&quot;,&quot;Description&quot;:&quot;The Harry Potter Film Concert Series returns to the
Esplanade Theatre in Singapore with Harry Potter and the Goblet of Fire™ in Concert, the
fourth film in the Harry Potter series. On February 28th and 29th, 2020, the Metropolitan
Festival Orchestra will perform this magical score live from Harry Potter and the Goblet of
Fire™ while the entire film plays in high-definition on a 40-foot screen&quot;}
        print(&quot;the details of the event are:&quot;)
        print(&quot;&quot;)
        print(&quot;the available dates are:&quot;,details5[&quot;available dates&quot;])
        print(&quot;&quot;)
        print(&quot;the venue of the event is:&quot;,details5[&quot;venue&quot;])
        print(&quot;&quot;)
        print(&quot;the cost of tickets for the event are:&quot;,details5[&quot;Ticket price&quot;])
        print(&quot;&quot;)
        descchoice_music5=input(&quot;enter &#39;yes&#39; if you wish to view the description.enter &#39;no&#39; to
move onto the next step&quot;)
        if descchoice_music5==&quot;Yes&quot; or descchoice_music5==&quot;yes&quot;:
            print(&quot;the description of the event is:&quot;,details5[&quot;Description&quot;])
        elif descchoice_music5==&quot;no&quot; or descchoice_music5== &quot;No&quot;:
            print(&quot;The ticket information and invoice will soon be generated in the following
steps&quot;)      
 if genre==&quot;Sports&quot; or genre==&quot;sports&quot;:
   print(&quot;the list of upcoming sports events in singapore are:&quot;)
   sports_events=[&quot;Qualifiers-Singapore Badminton Open 2020&quot;,&quot;ASEAN Basketball
League:Singapore Slingers vs Heat&quot;,&quot;HSBC Singapore Sevens&quot;,&quot;Safari Zoo Run&quot;,&quot;Surf N
Sweat 2020&quot;]
   print(sports_events)
   print(&quot;select a sports event to view further information and details&quot;)
   sports_choice=input(&quot;Enter the name of the event you wish to view&quot;)

   if sports_choice==&quot;Qualifiers-Singapore Badminton Open 2020&quot;:
       sportsdetails1={&quot;available dates&quot;:&quot;07-04-2020&quot;,&quot;venue&quot;:&quot;Singapore Indoor
Stadium&quot;,&quot;Ticket price&quot;:&quot;$65&quot;,&quot;Description&quot;:&quot;World class shuttlers from around the globe will
battle it out at the Singapore Badminton Open 2020.Qualifying Round is on Tuesday, 7 April
2020, 10AM to 6PM.Preliminary round is on 8th April, 10 AM to 10PM. The finals is on 12th
April, 1PM to 7PM&quot;}
       print(&quot;the details of the event are:&quot;)
       print(&quot;the available dates are:&quot;,sportsdetails1[&quot;available dates&quot;])
       print(&quot;the venue of the event is:&quot;,sportsdetails1[&quot;venue&quot;])
       print(&quot;the cost of the tickets are:&quot;,sportsdetails1[&quot;Ticket price&quot;])
       descchoice_sports=input(&quot;enter &#39;yes&#39; if you wish to view the description. Enter &#39;no&#39; to
move onto the next step&quot;)
       if descchoice_sports==&quot;Yes&quot; or descchoice_sports==&quot;yes&quot;:
           print(&quot;the description of the event is&quot;,sportsdetails1[&quot;Description&quot;])
       if descchoice_sports==&quot;no&quot; or descchoice_sports==&quot;no&quot;:
           print(&quot;the invoice will be generated after ticket confirmation in the following steps&quot;)
      
   if sports_choice==&quot;ASEAN Basketball League:Singapore Slingers vs Heat&quot;:
       sportsdetails2={&quot;available dates&quot;:&quot;29-01-2020&quot;,&quot;venue&quot;:&quot;OCBC Arena&quot;,&quot;Ticket
price&quot;:&quot;$55&quot;,&quot;Description&quot;:&quot;watch the Singapore Slingers light up the court at OCBC
Arena.Experience the unbelievable atmosphere &amp; top-class hoop action of a Singapore
Slingers home game. Experience the unbelievable atmosphere &amp; top-class hoop action of a
Singapore Slingers home game!! Singapore Slingers are primed to do battle in the 2019-20
ASEAN Basketball League as they compete against quality professional teams from the
Philippines, Indonesia, Malaysia, Vietnam, Thailand, Taiwan, China &amp; Hong Kong in what’s
set to be one of the most tightly contested ABL seasons ever.&quot;}
       print(&quot;the details of the event are:&quot;)
       print(&quot;the available dates are:&quot;,sportsdetails2[&quot;available dates&quot;])
       print(&quot;the venue of the event is:&quot;,sportsdetails2[&quot;venue&quot;])
       print(&quot;the cost of the tickets are:&quot;,sportsdetails2[&quot;Ticket price&quot;])
       descchoice_sports2=input(&quot;enter &#39;yes&#39; if you wish to view the description. Enter &#39;no&#39; to
move to the next step&quot;)
       if descchoice_sports2==&quot;Yes&quot; or descchoice_sports2==&quot;yes&quot;:
           print(&quot;the description of the event is&quot;,sportsdetails2[&quot;Description&quot;])
       if descchoice_sports2==&quot;no&quot; or descchoice_sports2==&quot;no&quot;:
           print(&quot;the invoice will be generated after ticket confirmation in the following steps&quot;)
          
   if sports_choice==&quot;HSBC Singapore Sevens&quot;:
       sportsdetails3={&quot;available dates&quot;:&quot;11-04-2020,12-04-2020&quot;,&quot;venue&quot;:&quot;National
Stadium&quot;,&quot;Ticket price&quot;:&quot;$45&quot;,&quot;Description&quot;:&quot;The HSBC Singapore Rugby Sevens brings you
a weekend of world class entertainment. Held at the National Stadium on 11 and 12 April
2020, event-goers will enjoy two days of thrilling action on pitch and non-stop entertainment
off it.Fans will get to enjoy the short,fast form of rugby as 16 nations go head-to-head in their
quest to be crowned champions. Dubbed The Family Sevens for its family-centric format,
ticket holders will also enjoy an extensive line-up of off-pitch entertainment at the two-day
carnival, including a Family FunZone, Splash Party, rugby-themed games, live music and
lots more. Don’t miss the best show in town this April!&quot;}
       print(&quot;the details of the event are:&quot;)
       print(&quot;the available dates are:&quot;,sportsdetails3[&quot;available dates&quot;])
       print(&quot;the venue of the event is:&quot;,sportsdetails3[&quot;venue&quot;])
       print(&quot;the cost of the tickets are:&quot;,sportsdetails3[&quot;Ticket price&quot;])
       descchoice_sports3=input(&quot;enter &#39;yes&#39; if you wish to view the description. Enter &#39;no&#39; to
move to the next step&quot;)
       if descchoice_sports3==&quot;Yes&quot; or descchoice_sports3==&quot;yes&quot;:
           print(&quot;the description of the event is&quot;,sportsdetails3[&quot;Description&quot;])

       if descchoice_sports3==&quot;no&quot; or descchoice_sports3==&quot;no&quot;:
           print(&quot;the invoice will be generated after ticket confirmation in the following steps&quot;) 
   if sports_choice==&quot;Safari Zoo Run&quot;:
       sportsdetails4={&quot;available dates&quot;:&quot;29-03-2020&quot;,&quot;venue&quot;:&quot;Singapore Zoo&quot;,&quot;Ticket
price&quot;:&quot;$40&quot;,&quot;Description&quot;:&quot;Take part in the final edition of Safari Zoo Run before Mandai&#39;s
major makeover. Choose from the competitive Safari Zoo challenge, duo dash and junior
dash, or the easy Safari Zoo walk. Then pledge your allegiance to any one of Wildlife
Reserves Singapore’s four park icons: Jurong Bird Park’s Sunny the hornbill, Night Safari’s
Chawang the elephant, River Safari’s Canola the manatee and Singapore Zoo’s Ah Meng
the orangutan, and champion a conservation cause&quot;}
       print(&quot;the details of the event are:&quot;)
       print(&quot;the available dates are:&quot;,sportsdetails4[&quot;available dates&quot;])
       print(&quot;the venue of the event is:&quot;,sportsdetails4[&quot;venue&quot;])
       print(&quot;the cost of the tickets are:&quot;,sportsdetails4[&quot;Ticket price&quot;])
       descchoice_sports4=input(&quot;enter &#39;yes&#39; if you wish to view the description. Enter &#39;no&#39; to
move to the next step&quot;)
       if descchoice_sports4==&quot;Yes&quot; or descchoice_sports4==&quot;yes&quot;:
           print(&quot;the description of the event is&quot;,sportsdetails4[&quot;Description&quot;])
       if descchoice_sports4==&quot;no&quot; or descchoice_sports4==&quot;no&quot;:
           print(&quot;the invoice will be generated after ticket confirmation in the following steps&quot;)
          
   if sports_choice==&quot;Surf N Sweat 2020&quot;:
       sportsdetails5={&quot;available dates&quot;:&quot;07-03-2020,08-03-2020&quot;,&quot;venue&quot;:&quot;Nanyang
technological university&quot;,&quot;Ticket price&quot;:&quot;$45&quot;,&quot;Description&quot;:&quot;Surf N Sweat is Singapore&#39;s
largest annual beach sporting event, proudly organised by Nanyang Technological
University Sports Club. &#39;ll be making waves at Palawan Beach, Sentosa, so prepare yourself
for a day of adrenaline pumping and exhilarating activities happening on both sand and
sea!Get groovy on 8th March 2020 as we are doing it retro style for our 25th Anniversary!
Come and join us!&quot;}
       print(&quot;the details of the event are:&quot;)
       print(&quot;the available dates are:&quot;,sportsdetails5[&quot;available dates&quot;])
       print(&quot;the venue of the event is:&quot;,sportsdetails5[&quot;venue&quot;])
       print(&quot;the cost of the tickets are:&quot;,sportsdetails5[&quot;Ticket price&quot;])
       descchoice_sports5=input(&quot;enter &#39;yes&#39; if you wish to view the description. Enter &#39;no&#39; to
move to the next step&quot;)
       if descchoice_sports5==&quot;Yes&quot; or descchoice_sports5==&quot;yes&quot;:
           print(&quot;the description of the event is&quot;,sportsdetails5[&quot;Description&quot;])
       if descchoice_sports5==&quot;no&quot; or descchoice_sports5==&quot;no&quot;:
           print(&quot;the invoice will be generated after ticket confirmation in the following steps&quot;)
 
                   
    

import json
if genre==&quot;Art&quot; or genre==&quot;art&quot;:
   x=input(&quot;Type ‘exhibition’ or type ‘competition’ according to your preference&quot;)
   if x==&quot;exhibition&quot; or x==&quot;Exhibition&quot;:

       print(&quot;the list of upcoming art exhibitions in singapore are:&quot;)
       exhibitions=[&quot;Prospect.4&quot;,&quot;On the Horizon&quot;,&quot;A Dangerous Woman&quot;,&quot;About
Face&quot;,&quot;DuoX4Odell’s&quot;,&quot;Jamini Roy&quot;]
       print(exhibitions)
       dic1={&quot;available
dates&quot;:&quot;30/01/20,2/02/20,10/02/20,18/02/20,27/02/20,2/03/20,11/03/20,17/03/20,30/03/20&quot;,
&quot;Venue&quot;:&quot;F1 pit building&quot;,&quot;Price of adult ticket&quot;:&quot;$60&quot;,&quot;Price of child ticket&quot;:&quot;$45&quot;}      
dic2={&quot;available
dates&quot;:&quot;29/01/20,3/02/20,13/02/20,22/02/20,28/02/20,4/03/20,18/03/20&quot;,&quot;Venue&quot;:&quot;City
Hall&quot;,&quot;Price of adult ticket&quot;:&quot;$70&quot;,&quot;Price of child ticket&quot;:&quot;$55&quot;}
       dic3={&quot;available
dates&quot;:&quot;26/01/20,8/02/20,17/02/20,22/02/20,28/02/20,9/03/20,17/03/20&quot;,
&quot;Venue&quot;:&quot;Serangoon Nex&quot;,&quot;Price of adult ticket&quot;:&quot;$30&quot;,&quot;Price of child ticket&quot;:&quot;$20&quot;}
       dic4={&quot;available dates&quot;:&quot;24/01/20,3/02/20,10/02/20,28/02/20,9/03/20,17/03/20&quot;,
&quot;Venue&quot;:&quot;Baltimore’s Creative Alliance Main Gallery&quot;,&quot;Price of adult ticket&quot;:&quot;$30&quot;,&quot;Price of
child ticket&quot;:&quot;$20&quot;}
        
       dic5={&quot;available dates&quot;:&quot;26/01/20,7/02/20,16/02/20,25/02/20,,9/03/20,30/03/20&quot;,
&quot;Venue&quot;:&quot;Gotham City&quot;,&quot;Price of adult ticket&quot;:&quot;$50&quot;,&quot;Price of child ticket&quot;:&quot;$40&quot;}
       dic6={&quot;available
dates&quot;:&quot;25/01/20,7/02/20,15/02/20,22/02/20,28/02/20,17/03/20,29/03/20&quot;, &quot;Venue&quot;:&quot;Artwalk
Little India&quot;,&quot;Price of adult ticket&quot;:&quot;$80&quot;,&quot;Price of child ticket&quot;:&quot;$60&quot;}

   details=input(&quot;enter ‘yes’ in order to view description of events&quot;)
   if details==&quot;yes&quot; or details==&quot;Yes&quot;:
       event=input(&quot;enter the name of the event you wish to see a description of&quot;)
       if event==&quot;Prospect.4&quot;:
           print(&quot;The fourth iteration of this city-wide exhibition includes the works of 73 artists,
who are based primarily in the US, Caribbean, Latin America, and Europe. Organized by
curator Trevor Schoomaker, Prospect 4, includes everything from art and jazz museums to
an antique store and billboards, and is accompanied by over a 100 satellite exhibitions.&quot;)
       if event==&quot;On the Horizon&quot;:
           print(&quot;Internal Landscapes, the first iteration in the multipart On the Horizon, focuses
on a fraught motif in the Cuban historical and aesthetic cosmology, the​​ horizon, and
specifically how it relates to the body. The curation is intelligently expansive; the show
encompasses the many registers of diaspora and exile that frame the Cuban experience,
with works on view by artists born in Miami, artists born on the island and living there like
Yoan Capote, those based elsewhere like New York, and canonical Cuban-born, Miami-
based giants like José Bedia and Gory.&quot;)
       if event==&quot;A Dangerous Woman&quot;:
           print(&quot;A Dangerous Woman: at the Columbus Museum of Art (CMA) is the first survey
since the mid-20th century of the artist’s works, many of which are on loan from her estate,
and showcases a largely uncelebrated powerhouse of multiple styles, including Rockwell-
esque depictions of quotidian American life and unsettling, decidedly feminine Surrealist
portraiture. Credit is due to CMA for putting together a remarkable exhibition on a fascinating
artist worthy of deeper consideration.&quot;)
       if event==&quot;About Face&quot;:
           print(&quot;The group exhibition, About Face, at Baltimore’s Creative Alliance Main Gallery
featured four artists of color who, like Sherald, depict empowered black subjects that exude
a palpable sense of agency. The show featured Rozeal’s Japanese-inspired graphic scrolls,
Tim Okamura’s painterly realism, and Ebony G. Patterson’s baroque fiber-based wall

installations celebrating Jamaican dance culture. With Sherald’s romantic figures at the
center, About Face explored portraiture as an effective tool for envisioning a more inclusive
and authentic America, one created by diverse authors and devoid of tokenism and
exoticism. Together these portraits pointed toward a future art historical cannon where black
faces and figures are the rule, rather than the exception.&quot;)
       if event==&quot;DuoX4Odell’s&quot;:
           print(&quot;Daniel Wickerham and Malcolm Lomax, also known collaboratively as DUOX,
have been making theatrical, multi-media installations that use digital collage, animation,
interactive video, and web design to posit queer-centered narratives since 2009. For
Singapore’s second iteration of Light City, a citywide art and technology festival, the duo was
selected to explore Odell’s, a historic dance club that existed from 1976 to ’92 on North
Avenue and served as an exclusive cultural hub for the African American community.&quot;)
       if event==&quot;Jamini Roy&quot;:
           print(&quot;Jamini Roy (11 April 1887 – 24 April 1972) was an Indian painter. He was
honoured with the State award of Padma Bhushan in 1954. He was one of the most famous
pupils of Rabindranath Tagore, whose artistic originality and contribution to the emergence
of modern art in India remains unquestionable.&quot;)
   if details==&quot;no&quot;:
       facts=input(&quot;enter the event for show details&quot;)
       if facts==&quot;Prospect.4&quot;:
           print(json.dumps(dic1,indent=2))
       elif facts==&quot;On the Horizon&quot;:
           print(json.dumps(dic2,indent=2))
       elif facts==&quot;A Dangerous Woman&quot;:
           print(json.dumps(dic3,indent=2))
       elif facts==&quot;About Face&quot;:
           print(json.dumps(dic4,indent=2))
       elif facts==&quot;DuoX4Odell&#39;s&quot;:
           print(json.dumps(dic5,indent=2))
       elif facts==&quot;Jamini Roy&quot;:
           print(json.dumps(dic6,indent=2))
if x==&quot;competition&quot; or &quot;Competition&quot;:
        print(&quot;the list of upcoming art competitions in singapore are:&quot;)
        competitions=[&quot;Artshub&quot;,&quot;GIIS Art&quot;,&quot;RWCC&quot;,&quot;SOTA&quot;,&quot;UOB Painting of the Year&quot;]
        print(competitions)
        dicc1={&quot;Date&quot;:&quot;10/02/20&quot;, &quot;Venue&quot;:&quot;SINDA,Little India&quot;,&quot;Entry fees for Juniors(5-
10yrs)&quot;:&quot;$20-solo,$15-group&quot;,&quot;Entry fees for Senior(11-17yrs)&quot;:&quot;$30-solo,$20-
group&quot;,&quot;Categories&quot;:&quot;Classical, Folk, Fusion&quot;}
        dicc2=dict(zip((&quot;Date&quot;,&quot;Venue&quot;,&quot;Entry fees for Junior(8-12yrs)&quot;,&quot;Entry fees for
Senior(13-19yrs)&quot;,&quot;Categories&quot;),(&quot;15/05/20&quot;,&quot;Esplanade&quot;,&quot;$30-solo,$30-group&quot;,&quot;$30-
solo,$30-group&quot;,&quot;Classical, Folk, Contemporary&quot;)))
        dicc3=dict(((&quot;Date&quot;,&quot;18/02/20&quot;), (&quot;Venue&quot;,&quot;Edgefield primary School&quot;),(&quot;Entry fees for
Junior(5-10yrs)&quot;,&quot;$30-solo,$35-group&quot;),(&quot;Entry fees for Senior(11-19yrs)&quot;,&quot;$40-solo,$35-
group&quot;),(&quot;Categories&quot;,&quot;Semi-Classical, Folk, Fusion&quot;)))
        dicc4=dict(([&quot;Date&quot;,&quot;11/06/20&quot;], [&quot;Venue&quot;,&quot;Global Indian International School&quot;],[&quot;Entry
fees for Junior(9-15yrs)&quot;,&quot;$10-solo,$15-group&quot;],[&quot;Entry fees for Senior(16-24yrs)&quot;,&quot;$20-
solo,$15-group&quot;],[&quot;Categories&quot;,&quot;Semi-Classical, International folk, Fusion&quot;]))
        dicc5={&quot;Date&quot;:&quot;30/07/20&quot;, &quot;Venue&quot;:&quot;Yishun JC&quot;,&quot;Entry fees for Junior(7-13yrs)&quot;:&quot;$20-
solo,$25-group&quot;,&quot;Entry fees for Senior(14-20yrs)&quot;:&quot;$30-solo,$20-
group&quot;,&quot;Categories&quot;:&quot;Classical, Folk, Hip-hop&quot;}
        artdetail1=input(&quot;enter the event you wish to view the details of&quot;)
        if artdetail1==&quot;Artshub&quot;:
              print(&quot;Artshub initiate to create an interactive platform to promote the finest artwork
of all well-known artists, in order to gain the recognition they deserve.  Arts Hub Singapore is

to promote art and artists to an international platform. Their aim is to promote arts activities
that inspire young people with a lasting enthusiasm for the arts, art awareness of our arts
heritage and its conservation and to expand the horizons of young people through their
involvement in creative arts.&quot;)
              print(&quot;Date of event:&quot;,dicc1[&quot;Date&quot;])
              print(&quot;Venue:&quot;,dicc1[&quot;Venue&quot;])
              print(&quot;Categories:&quot;,dicc1[&quot;Categories&quot;])
              print(&quot;Entry fees for Juniors:&quot;,dicc1[&quot;Entry fees for Juniors(5-10yrs)&quot;])
              print(&quot;Entry fees for Seniors:&quot;,dicc1[&quot;Entry fees for Senior(11-17yrs)&quot;])
        if artdetail1==&quot;GIIS Art&quot;:
              print(&quot;GIIS promotes budding artists and inspires them to think out of the box and
bring out their best.&quot;)
              print(&quot;Date of event:&quot;,dicc2[&quot;Date&quot;])
              print(&quot;Venue:&quot;,dicc2[&quot;Venue&quot;])
              print(&quot;Categories:&quot;,dicc2[&quot;Categories&quot;])
              print(&quot;Entry fees for Juniors:&quot;,dicc2[&quot;Entry fees for Junior(8-12yrs)&quot;])
              print(&quot;Entry fees for Seniors:&quot;,dicc2[&quot;Entry fees for Senior(13-19yrs)&quot;])
        if artdetail1==&quot;RWCC&quot;:
              print(&quot;Real World Challenges Conventions is an extraordinary platform that
challenges the ability of students to think .&quot;)
              print(&quot;Date of event:&quot;,dicc3[&quot;Date&quot;])
              print(&quot;Venue:&quot;,dicc3[&quot;Venue&quot;])
              print(&quot;Categories:&quot;,dicc3[&quot;Categories&quot;])
              print(&quot;Entry fees for Juniors:&quot;,dicc3[&quot;Entry fees for Junior(5-10yrs)&quot;])
              print(&quot;Entry fees for Seniors:&quot;,dicc3[&quot;Entry fees for Senior(11-19yrs)&quot;])
        if artdetail1==&quot;SOTA&quot; :
              print(&quot;SOTA is pleased to announce the third edition of its annual nation-wide
drawing and painting competition. This year, the SOTA Primary 6 Art Competition is proudly
supported by Mapletree.&quot;)
              print(&quot;Date of event:&quot;,dicc4[&quot;Date&quot;])
              print(&quot;Venue:&quot;,dicc4[&quot;Venue&quot;])
              print(&quot;Categories:&quot;,dicc4[&quot;Categories&quot;])
              print(&quot;Entry fees for Juniors:&quot;,dicc4[&quot;Entry fees for Junior(9-15yrs)&quot;])
              print(&quot;Entry fees for Seniors:&quot;,dicc4[&quot;Entry fees for Senior(16-24yrs)&quot;])
        if artdetail1==&quot;UOB Painting of the Year&quot; :
              print(&quot;Driven by a passion to encourage talented artists in their creative pursuits,
United Overseas Bank (UOB) started the Painting of the Year competition in Singapore in
1982. Today, the annual art competition is the longest-running in Singapore and one of the
most prestigious in Southeast Asia&quot;)
              print(&quot;Date of event:&quot;,dicc5[&quot;Date&quot;])
              print(&quot;Venue:&quot;,dicc5[&quot;Venue&quot;])
              print(&quot;Categories:&quot;,dicc5[&quot;Categories&quot;])
              print(&quot;Entry fees for Juniors:&quot;,dicc5[&quot;Entry fees for Junior(7-13yrs)&quot;])
              print(&quot;Entry fees for Seniors:&quot;,dicc5[&quot;Entry fees for Senior(14-20yrs)&quot;])
              print(&quot;We invite pupils (who will be in Primary 6 in 2020) who are creative and
budding artists to participate in this visual arts competition.&quot;)

listofevents=[‘Dance’,’Music’,’Sports’,’Artexhibitions’,’Artcompetitions’]
dance_events=[&#39;Ultra Singapore&#39;,&#39;Atara: For you&#39;,&#39;Dance Appreciation Series&#39;, &#39;Dancing
Maidens&#39;]
music_events=[&#39;Songkran music festival&#39;,&#39;Stereofest&#39;,&#39;Hydeout Music Festival&#39;,&#39;Shakti&#39;,&#39;Harry
Potter and the Goblet of Fire-Concert&#39;]

sports_events=[&#39;Qualifiers-Singapore Badminton Open 2020&#39;,&#39;ASEAN Basketball League:
Singapore Slingers vs Heat&#39;,&#39;HSBC Singapore Sevens&#39;,&#39;Safari Zoo Run&#39;,&#39;Surf N Sweat 2020&#39;]
art_events=[&quot;Prospect.4&quot;,&quot;On the Horizon&quot;,&quot;A Dangerous Woman&quot;,&quot;About
Face&quot;,&quot;DuoX4Odell’s&quot;,&quot;Jamini Roy&quot;]
arts_events=[&quot;Artshub&quot;,&quot;GIIS Art&quot;,&quot;RWCC&quot;,&quot;SOTA&quot;,&quot;UOB Painting of the Year&quot;]

a=input(&quot;enter the genre of event you want to choose&quot;)
booking_fee=60
print(&quot;the booking fee for the events is&quot;,booking_fee)
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
    print(&quot;enter the dance event from the following&quot;,dance_events)
    select_dance=input(&quot;enter the dance event you wish to select&quot;)
    print(select_dance)
    if select_dance==&#39;Ultra Singapore&#39;:
        print(&quot;the total charge is:&quot; ,ticketprice_dance1+booking_fee)
        ticketprice+=1
    if select_dance==&#39;Atara: For you&#39;:
        print(&quot;the total charge is:&quot; ,ticketprice_dance2+booking_fee)
        ticketprice+=1
    if select_dance==&#39;Dance Appreciation 
Series&#39;:
        print(&quot;the total charge is:&quot; ,ticketprice_dance3+booking_fee)
        ticketprice+=1
    if select_dance==&#39;Dancing Maidens&#39;:
        print(&quot;the total charge is:&quot; ,ticketprice_dance4+booking_fee)
        ticketprice+=1
        

def my_musicfunction():
    ticketprice=0
    print(&quot;enter the music event from the following&quot;,music_events)
    select_music=input(&quot;enter the music event you wish to select&quot;)
    print(select_music)
    if select_music==&#39;Songkran music festival&#39;:
        print(&quot;the total charge is:&quot; ,ticketprice_music1+booking_fee)
    if select_music==&#39;Stereofest&#39;:
        print(&quot;the total charge is:&quot; ,ticketprice_music2+booking_fee)
    if select_music==&#39;Hydeout Music Festival&#39;:
        print(&quot;the total charge is:&quot; ,ticketprice_music3+booking_fee)
    if select_music==&#39;Shakti&#39;:
        print(&quot;the total charge is:&quot; ,ticketprice_music4+booking_fee)
    if select_music==&#39;Harry Potter and the Goblet of Fire-Concert&#39;:
        print(&quot;the total charge is:&quot; ,ticketprice_music5+booking_fee)

def my_sportsfunction():
    print(&quot;enter the sports event from the following&quot;,sports_events)
    select_sports=input(&quot;enter the sports event you wish to select&quot;)
    print(select_sports)
    if select_sports==&#39;Qualifiers-Singapore Badminton Open 2020&#39;:
        print(&quot;the total charge is:&quot; ,ticketprice_sports1+booking_fee)
    if select_sports==&#39;ASEAN Basketball League: Singapore Slingers vs Heat&#39;:
        print(&quot;the total charge is:&quot; ,ticketprice_sports2+booking_fee)
    if select_sports==&#39;HSBC Singapore Sevens&#39;:
        print(&quot;the total charge is:&quot; ,ticketprice_sports3+booking_fee)
    if select_sports==&#39;Safari Zoo Run&#39;:
        print(&quot;the total charge is:&quot; ,ticketprice_sports4+booking_fee)
    if select_sports==&#39;Surf N Sweat 2020&#39;:
        print(&quot;the total charge is:&quot; ,ticketprice_sports5+booking_fee)
def my_artfunction():
    print(&quot;enter the art event from the following&quot;,art_events)
    select_art=input(&quot;enter the art event you wish to select&quot;)
    print(select_art)
    if select_art==&#39;Prospect.4&#39;:
        print(&quot;the total charge for child is:&quot; ,ticketprice_childart1+booking_fee)
        print(&quot;the total charge for adult is:&quot; ,ticketprice_adultart1+booking_fee)
        
    if select_art==&#39;On the Horizon&#39;:
        print(&quot;the total charge for child is:&quot; ,ticketprice_childart2+booking_fee)
        print(&quot;the total charge for adult is:&quot; ,ticketprice_adultart2+booking_fee)
        
    if select_art==&#39;A Dangerous Woman&#39;:
        print(&quot;the total charge for child is:&quot; ,ticketprice_childart3+booking_fee)
        print(&quot;the total charge for adult is:&quot; ,ticketprice_adultart3+booking_fee)
        
    if select_art==&#39;About Face&#39;:
        print(&quot;the total charge for child is:&quot; ,ticketprice_childart4+booking_fee)
        print(&quot;the total charge for adult is:&quot; ,ticketprice_adultart4+booking_fee)
       
    if select_art==&#39;DuoX4Odell’s&#39;:
        print(&quot;the total charge for child is:&quot; ,ticketprice_childart5+booking_fee)
        print(&quot;the total charge for adult is:&quot; ,ticketprice_adultart5+booking_fee)
        
    if select_art==&#39;Jamini Roy&#39;:
       print(&quot;the total charge for child is:&quot; ,ticketprice_childart6+booking_fee)
       print(&quot;the total charge for adult is:&quot; ,ticketprice_adultart6+booking_fee)
        
def my_artsfunction():
    print(&quot;enter the art event from the following&quot;,arts_events)
    select_arts=input(&quot;enter the dance event you wish to select&quot;)
    print(select_arts)
    if select_arts==&#39;ArtsHub&#39;:
        print(&quot;the total charge for junior solo is:&quot; ,ticketprice_juniorsolo1+booking_fee)
        print(&quot;the total charge for junios group is:&quot; ,ticketprice_juniorgroup1+booking_fee)
        print(&quot;the total charge for senior solo is:&quot; ,ticketprice_seniorsolo1+booking_fee)
        print(&quot;the total charge for senior group is:&quot; ,ticketprice_seniorgroup1+booking_fee)
        ticketprice+=1
    if select_arts==&#39;GIIS Art&#39;:

        print(&quot;the total charge for junior solo is:&quot; ,ticketprice_juniorsolo2+booking_fee)
        print(&quot;the total charge for junior group is:&quot; ,ticketprice_juniorgroup2+booking_fee)
        print(&quot;the total charge for senior solo is:&quot; ,ticketprice_seniorsolo2+booking_fee)
        print(&quot;the total charge for senior group is:&quot; ,ticketprice_seniorgroup2+booking_fee)
        ticketprice+=1
    if select_arts==&#39;RWCC&#39;:
        print(&quot;the total charge for junior solo is:&quot; ,ticketprice_juniorsolo3+booking_fee)
        print(&quot;the total charge for junior group is:&quot; ,ticketprice_juniorgroup3+booking_fee)
        print(&quot;the total charge for senior solo is:&quot; ,ticketprice_seniorsolo3+booking_fee)
        print(&quot;the total charge for senior group is:&quot; ,ticketprice_seniorgroup3+booking_fee)
        ticketprice+=1
    if select_arts==&#39;SOTA&#39;:
        print(&quot;the total charge for junior solo is:&quot; ,ticketprice_juniorsolo4+booking_fee)
        print(&quot;the total charge for junior group is:&quot; ,ticketprice_juniorgroup4+booking_fee)
        print(&quot;the total charge for senior solo is:&quot; ,ticketprice_seniorsolo4+booking_fee)
        print(&quot;the total charge for senior group is:&quot; ,ticketprice_seniorgroup4+booking_fee)
        ticketprice+=1
        
    if select_arts==&#39;UOB Painting of the Year&#39;:
        print(&quot;the total charge for junior solo is:&quot; ,ticketprice_juniorsolo5+booking_fee)
        print(&quot;the total charge for junior group is:&quot; ,ticketprice_juniorgroup5+booking_fee)
        print(&quot;the total charge for senior solo is:&quot; ,ticketprice_seniorsolo5+booking_fee)
        print(&quot;the total charge for senior group is:&quot; ,ticketprice_seniorgroup5+booking_fee)
        ticketprice+=1

    
for i in listofevents:
    if i==a:
        print(&quot;the event you have chosen is&quot;,i)
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
    print(&quot;Thank You for using EVENTFUL”)
    n=input(&quot;enter yes for feedback&quot;)
    if n==&quot;yes&quot;:

        x=input(&quot;enter feedback&quot;)
        print(&quot;Thank you for your feedback&quot;)
        print(&quot;ticket info&quot;)
    else:
        print(&quot;ticket info&quot;)
thankyou()
