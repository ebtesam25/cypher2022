## 📚 What does ImmiGrace do?
   
   ImmiGrace is a curated and scalable list of resources for immigrants of all kinds with its own search engine. On top of its own search engine, ImmiGrace includes an interactive SMS chatbot that helps its users to receive guidance, and query ImmiGrace's vast list of resources. 

   ImmiGrace includes countless resources from immigrants with a variety of categories. These categories range from Local Legal Help to global scholarships only for immigrants. ImmiGrace is built to be scalable as it imports the list of resources from a google sheet that anyone can add resources to. 

## 💡 What Inspired Us?

**Here is an anecdote from our team member, Musa Oguzhan (Olsen):**

   "I have faced countless challenges because of my legal status. These challenges range from minor annoyances like having to renew my drivers license every 8 months to not being eligible for any kind of federal financial aid (student loans/grants), and most scholarships. My college journey has been quite difficult due to these challenges. 

   I started my college journey at Virginia Tech, majoring in Computer Science. I was at the top of my class after completing freshman year with a 4.0, leading an engineering design team. With all these accomplishments, I still did not know if I could keep attending Virginia Tech since the lack of financial aid/scholarships and guidance for people like me. So, I decided to google organizations who could help me with my situation.

   Although there were many resources online, they were scattered all over the web. This has led me to spending more time trying to find scholarships/helpful organizations than I was spending studying for my classes. After countless hours of applying for scholarships, I was able to receive the Golden Door Scholarship that granted me a full ride to transfer to Davidson College.

   Throughout my journey, I always wished that there was a centralized hub of curated resources for people like myself. This hub would have saved me so much time, helping me through my college journey. 

   We have built ImmiGrace to do exactly this. ImmiGrace is the resource I wish I had when I first started struggling with the challenges that came with my legal status." 

## 🤷‍♂️ How we built ImmiGrace?

   We built ImmiGrace as a web-app with React.js. It has a reactive UI that will function in any type of device.  We store our user & resource data in CockroachDB, and access it through Google cloud serverless functions. 

   Our chatbot is built with Twilio, and it interacts with our CockroachDB through Google cloud serverless functions just like our frontend. Users can SMS our chatbot to reach our resources faster, and in a more accessible manner.

   To ensure that our resource data is scalable, we created a google sheet that everyone can append to. To import the sheet to our website, we export it as a .csv file and then convert it to a JSON file. 

   Lastly, we used Google Cloud Computing's translation API to ensure that our resources were translated to the language of our users choice, making our application accessible even further. 

## 🌼 WMFIRE Challenge

🚨Easy to use:

   We put a great thought into making our program easy to use, and accessible for people of variety of backgrounds. Our application has a simple login/registration page. After logging in, all resources presented to you with no additional clicks. There is a search bar at the top right corner which makes searching for resources a lot easier. Our automatic translation system translates these resources to the language of your choice, which makes our application even easier to use. Lastly, if the web ui is overwhelming, our Twilio bot makes interacting with our database from your phone frictionless and trouble free!

🚨Organized Selection of Resources: 

   All our resources have a category, and automatically generated tags that can be queried through our own search engine. This makes finding resources quite simple, and intuitive. You just have to have an idea of what you are looking for, our tags/search engine should handle the rest!

🚨Easy to Continue: 

   We made sure that our application was scalable, so that anyone can pick up where we left and grow ImmiGrace. Our resources are stored on a google sheet, which we later import as a .csv and lastly as a JSON file to directly feed to our application. Anyone can add to this google sheet, then convert the data to be usable on our system. 

## 💻 Our Tech Stack

**Frontend**
* React

![react](https://cdn2.iconfinder.com/data/icons/designer-skills/128/react-256.png)

**Backend**
* CockroachDB 
* Google Cloud Computing
* Python 
* Twilio

![](https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco,dpr_1/hguvdothzqqj8gfvozy8)
![](https://seeklogo.com/images/G/google-cloud-functions-logo-AECD57BFA2-seeklogo.com.png)
![](https://cdn.iconscout.com/icon/free/png-256/python-2752092-2284909.png)
![](https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_256,w_256,f_auto,q_auto:eco,dpr_1/zy6ttel4bwjtojwcf3cu)

**Version Control & Package Manager**
* GitHub
* Yarn

![](https://b.thumbs.redditmedia.com/AltCa25flSy96k0VDTcXUseNPu25FWaInEl1LOvkbqs.png)
![](https://upload.wikimedia.org/wikipedia/en/3/39/Yarn_logo.png)

