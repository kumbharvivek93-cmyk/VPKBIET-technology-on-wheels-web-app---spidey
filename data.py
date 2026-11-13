"""All editable website content lives here. Items marked EDITABLE are placeholders.
Text for About / Vision / Mission / Activities / Team comes from your supplied files."""

SITE = {"name": "Technology on Wheels", "short": "ToW", "college": "VPKBIET",
        "tagline": "Bringing Innovation, Learning & Inspiration to Every School"}

NAV = [("Home", "index"), ("About", "about"), ("Learning Activities", "learning_activities"),
       ("Project Gallery", "project_gallery"), ("Contact", "contact"), ("Feedback", "feedback")]

HERO = {"title": "Technology on Wheels", "subtitle": SITE["tagline"], "credit": "An Initiative of VPKBIET",
        "btn1": "Explore Our Journey", "btn2": "Learn More"}

HIGHLIGHTS = [("🤖", "Robotics & AI workshops"), ("💻", "Coding & electronics activities"),
              ("🔬", "Science & technology exhibitions"), ("💡", "Student innovation projects"),
              ("🎓", "Career awareness & inspiration sessions")]

STEPS = [("🚌", "Bus reaches school"), ("🔍", "Students explore activities"),
         ("🛠️", "Hands-on learning"), ("🚀", "Inspiration & innovation")]

HOME_MISSION = ("Technology on Wheels is a VPKBIET initiative to take technology, innovation, and "
                "practical learning directly to schools and students across India.")

WHY = "To remove geographical and financial barriers that keep rural students away from modern STEM infrastructure."  # EDITABLE
VPKBIET_ROLE = ("The bus is launched by Vidya Pratishthan's Sharadchandra Pawar Centre of Excellence in "
                "Artificial Intelligence (VPSPCOE), with VPKBIET students contributing to the initiative's website.")  # EDITABLE
AUDIENCE = [("🎒", "School students"), ("👩‍🏫", "Teachers"), ("🏫", "Schools"), ("🌾", "Rural & urban communities")]
GOALS = ["Curiosity", "Practical learning", "Innovation", "Digital literacy", "Future-ready skills"]

TIMELINE = [("June 2026", "Technology on Wheels bus inaugurated in Pune by Sharad Pawar, with Supriya Sule and Prataprao Pawar."),
            ("Launch", "Started by VPSPCOE-AI in collaboration with Sakal Media Group."),
            ("Next", "School visits across rural and remote regions (EDITABLE: add dates and schools).")]

CONTACT = {"email": "vpspcoe.ai@vidyapratishthan.com", "phone": "91 2112 239504",  # EDITABLE
           "address": "VPKBIET, Vidyanagari, MIDC, Baramati, Pune, Maharashtra 413133",  # EDITABLE
           "college": "Vidya Pratishthan's Kamalnayan Bajaj Institute of Engineering & Technology (VPKBIET)",
           "map_query": "VPKBIET Baramati",
           "social": [("Instagram", "#"), ("YouTube", "#"), ("LinkedIn", "#"), ("Facebook", "#")]}

# Gallery: first group uses your real photos (static/img/gallery). Others are EDITABLE placeholders (no image -> icon).
PROJECTS = [
 {"title": "Inauguration of the ToW Bus", "cat": "Inauguration", "img": "bus-group.jpg", "team": "VPSPCOE & Sakal Media Group", "desc": "Guests and organisers gather in front of the Technology on Wheels bus in Pune."},
 {"title": "Inauguration Group Photo", "cat": "Inauguration", "img": "group-wide.jpg", "team": "VPSPCOE & Sakal Media Group", "desc": "The launch team and dignitaries beside the bus."},
 {"title": "Dignitaries at the Launch", "cat": "Inauguration", "img": "group-bus2.jpg", "team": "VPSPCOE", "desc": "Chief guests and faculty at the inauguration in June 2026."},
 {"title": "Inauguration Ceremony", "cat": "Inauguration", "img": "stage.jpg", "team": "VPSPCOE", "desc": "Speeches and felicitation during the inauguration programme."},
 {"title": "Guests Interacting", "cat": "Inauguration", "img": "guests.jpg", "team": "VPSPCOE", "desc": "Guests during the ceremony."},
 {"title": "Technology on Wheels Bus", "cat": "Inauguration", "img": "bus-yard.jpg", "team": "VPSPCOE", "desc": "The robotic bus with the launch team."},
 {"title": "Inside the Bus: Live Demos", "cat": "Inside the Bus", "img": "inside1.jpg", "team": "VPSPCOE", "desc": "Guests exploring the onboard exhibits and the interactive robot."},
 {"title": "Exploring the Mobile Lab", "cat": "Inside the Bus", "img": "inside2.jpg", "team": "VPSPCOE", "desc": "Hands-on demonstrations of AI, Robotics and AR."},
 {"title": "Robot Guide Demonstration", "cat": "Inside the Bus", "img": "inside3.jpg", "team": "VPSPCOE", "desc": "The onboard interactive robot explaining the systems."},
 {"title": "Technology Showcase", "cat": "Inside the Bus", "img": "inside4.jpg", "team": "VPSPCOE", "desc": "Visitors learning about the exhibits."},
 {"title": "Line-Follower Robot", "cat": "Robotics", "img": "", "icon": "🤖", "team": "School Team A (EDITABLE)", "desc": "Placeholder project. Replace with a real student project."},
 {"title": "Crop Disease Detector", "cat": "AI", "img": "", "icon": "🧠", "team": "School Team B (EDITABLE)", "desc": "Placeholder project. Replace with a real student project."},
 {"title": "Smart Irrigation", "cat": "IoT", "img": "", "icon": "📡", "team": "School Team C (EDITABLE)", "desc": "Placeholder project. Replace with a real student project."},
 {"title": "Blinking LED Game", "cat": "Electronics", "img": "", "icon": "💡", "team": "School Team D (EDITABLE)", "desc": "Placeholder project. Replace with a real student project."},
 {"title": "Volcano Model", "cat": "Science", "img": "", "icon": "🔬", "team": "School Team E (EDITABLE)", "desc": "Placeholder project. Replace with a real student project."},
 {"title": "Quiz App", "cat": "Coding", "img": "", "icon": "💻", "team": "School Team F (EDITABLE)", "desc": "Placeholder project. Replace with a real student project."},
 {"title": "Solar Water Pump", "cat": "Innovation", "img": "", "icon": "☀️", "team": "School Team G (EDITABLE)", "desc": "Placeholder project. Replace with a real student project."},
]

FEEDBACK_SAMPLES = [  # EDITABLE placeholders
 {"name": "Student, Class 8", "role": "Student", "rating": 5, "text": "I saw a real robot talk to us! I want to learn coding now."},
 {"name": "Science Teacher", "role": "Teacher", "rating": 5, "text": "The AR demos made difficult topics easy for my students."},
 {"name": "Parent", "role": "Parent", "rating": 4, "text": "A wonderful way to bring modern technology to our village."},
]

ACTIVITIES = [{'age': 'Classes 6–12',
  'details': 'Artificial Intelligence and Machine Learning form the core intelligence of the mobile lab. AI '
             'refers to computer systems designed to perform tasks that typically require human '
             'intelligence, such as visual perception, speech recognition, and decision-making. Machine '
             'Learning is a subset of AI that enables software applications to learn from data and improve '
             'their accuracy over time without being explicitly programmed. Inside the bus, students '
             'interact with live AI models, including an AI-enabled guide robot that welcomes visitors and '
             'explains the onboard systems. The demonstrations show how algorithms recognize faces, process '
             'natural language, and classify objects in real time. Students learn how raw data is collected, '
             'cleaned, and fed into neural networks to train predictive models. Practical use cases tailored '
             'for rural communities, such as AI-driven crop disease detection and weather forecasting, are '
             'highlighted. The setup also introduces concepts like computer vision and edge AI, showing how '
             'smart devices make instant decisions locally without needing constant cloud connectivity. By '
             'interacting directly with these systems, students understand the difference between '
             'traditional rule-based coding and adaptive learning systems. This foundation helps demystify '
             'AI and encourages young learners to explore data science and algorithm development.',
  'duration': '20–30 min',
  'icon': '🧠',
  'short': 'Artificial Intelligence and Machine Learning form the core intelligence of the mobile lab. AI '
           'refers to computer systems designed to perform tasks that typically require human intelligence, '
           'such as visual perception, speech recognition, and decision-making.',
  'title': 'Artificial Intelligence (AI) and Machine Learning (ML)'},
 {'age': 'Classes 5–12',
  'details': 'Robotics and Automation focus on the design, construction, operation, and programming of '
             'intelligent machines that perform physical tasks. Robotics combines mechanical engineering, '
             'electronics, and computer science to build machines capable of interacting with the physical '
             'world. Automation uses control systems, such as Programmable Logic Controllers (PLCs), to '
             'operate industrial equipment with minimal human intervention. Inside the Technology on Wheels '
             'bus, students observe articulated robotic arms and mobile robots executing precise movements. '
             "The exhibits demonstrate how sensors act as the robot's eyes and ears, sending feedback to "
             'microcontrollers to guide picking, placing, and sorting actions. Students are introduced to '
             'block-based and text-based programming interfaces used to control robotic trajectories and '
             'speeds. The module also covers industrial automation concepts, showing how automated assembly '
             'lines increase safety, speed, and manufacturing precision. Learners see firsthand how '
             'collaborative robots (cobots) work safely alongside humans in modern factories. Understanding '
             'these principles prepares students for careers in smart manufacturing, mechatronics, and '
             'automated engineering.',
  'duration': '20–30 min',
  'icon': '🤖',
  'short': 'Robotics and Automation focus on the design, construction, operation, and programming of '
           'intelligent machines that perform physical tasks. Robotics combines mechanical engineering, '
           'electronics, and computer science to build machines capable of interacting with the physical '
           'world.',
  'title': 'Robotics and Automation'},
 {'age': 'Classes 7–12',
  'details': 'The Internet of Things (IoT) refers to a network of physical objects embedded with sensors, '
             'software, and connectivity that allows them to collect and exchange data over the internet. In '
             'the mobile bus, IoT is demonstrated through interconnected smart devices that monitor '
             'environmental conditions like temperature, humidity, soil moisture, and air quality. Students '
             'learn how microcontrollers—such as Arduino and Raspberry Pi—read analog and digital signals '
             'from physical sensors and transmit that information to cloud dashboards. The exhibits show how '
             'remote monitoring and control work in practice, such as turning on irrigation pumps '
             'automatically when soil moisture drops below a set threshold. Learners also explore Industrial '
             'IoT (IIoT), where machine health and energy consumption are tracked in real time to prevent '
             'equipment breakdowns. The curriculum emphasizes how low-cost sensors and wireless '
             'communication protocols like Wi-Fi, Bluetooth, and LoRaWAN connect everyday objects. Through '
             'live data visualization screens, students watch physical changes in the bus translate '
             'instantly into digital graphs. This hands-on exposure illustrates how IoT powers smart homes, '
             'precision agriculture, and connected cities.',
  'duration': '15–25 min',
  'icon': '📡',
  'short': 'The Internet of Things (IoT) refers to a network of physical objects embedded with sensors, '
           'software, and connectivity that allows them to collect and exchange data over the internet. In '
           'the mobile bus, IoT is demonstrated through interconnected smart devices that monitor '
           'environmental conditions like temperature, humidity, soil moisture, and air quality.',
  'title': 'Internet of Things (IoT)'},
 {'age': 'Classes 5–12',
  'details': 'Augmented Reality (AR) is an interactive technology that overlays digital information—such as '
             '3D models, animations, text, and sounds—onto the real-world environment. Unlike technologies '
             'that replace reality, AR enhances what a user sees through smartphones, tablets, or '
             'specialized smart glasses. Inside the Technology on Wheels bus, students use AR-enabled '
             'screens and tablets to explore complex scientific and engineering concepts in three '
             'dimensions. For example, pointing a device at a flat diagram in a textbook can bring a beating '
             'human heart, a working internal combustion engine, or the solar system to life on the screen. '
             'Students can rotate, zoom in, and dissect virtual layers of machinery without needing '
             'expensive physical prototypes. The demonstrations show how spatial computing and marker '
             'tracking anchor digital graphics accurately onto physical surfaces. Learners also see how AR '
             'is used in industrial maintenance to guide technicians step-by-step during complex repairs. By '
             'turning abstract textbook diagrams into interactive visual experiences, AR makes STEM subjects '
             'much easier to grasp and retain.',
  'duration': '10–15 min',
  'icon': '🕶️',
  'short': 'Augmented Reality (AR) is an interactive technology that overlays digital information—such as 3D '
           'models, animations, text, and sounds—onto the real-world environment. Unlike technologies that '
           'replace reality, AR enhances what a user sees through smartphones, tablets, or specialized smart '
           'glasses.',
  'title': 'Augmented Reality (AR)'},
 {'age': 'Classes 6–12',
  'details': 'Virtual Reality (VR) creates a completely simulated, three-dimensional digital environment '
             'that immerses the user and blocks out the physical world. Using head-mounted displays (VR '
             'headsets) and motion-tracking hand controllers, users can look around, walk through, and '
             'interact with virtual spaces as if they were physically there. In the mobile technology bus, '
             'VR stations transport rural students into virtual science laboratories, outer space, '
             'historical monuments, and advanced manufacturing plants. Students can safely perform virtual '
             'chemistry experiments or practice operating heavy industrial machinery without any physical '
             'risk or material waste. The setup demonstrates how stereoscopic displays, gyroscopes, and '
             'accelerometers track head and hand movements in real time to create a convincing sense of '
             'presence. Educators explain how VR is revolutionizing fields beyond gaming, including medical '
             'surgery training, architectural walkthroughs, and remote skill development. Experiencing VR '
             'firsthand sparks curiosity and shows students how digital simulations are built using 3D game '
             'engines and spatial design tools.',
  'duration': '10–15 min',
  'icon': '🥽',
  'short': 'Virtual Reality (VR) creates a completely simulated, three-dimensional digital environment that '
           'immerses the user and blocks out the physical world. Using head-mounted displays (VR headsets) '
           'and motion-tracking hand controllers, users can look around, walk through, and interact with '
           'virtual spaces as if they were physically there.',
  'title': 'Virtual Reality (VR)'},
 {'age': 'Classes 6–12',
  'details': '3D Printing, formally known as additive manufacturing, is the process of creating solid '
             'three-dimensional physical objects from a digital Computer-Aided Design (CAD) file. Unlike '
             'traditional subtractive manufacturing—which cuts or drills material away from a solid block—3D '
             'printing builds objects layer by layer from the bottom up. Inside the bus, live desktop 3D '
             'printers demonstrate Fused Deposition Modeling (FDM) by melting thermoplastic filaments like '
             'PLA and extruding them through a heated nozzle onto a build plate. Students observe the '
             'complete workflow, starting from designing a 3D model on a computer, slicing it into '
             'horizontal layers using specialized software, and watching the printer fabricate the part in '
             'real time. The exhibits showcase a variety of printed prototypes, mechanical gears, '
             'architectural models, and custom medical aids. Instructors highlight how 3D printing reduces '
             'material waste, speeds up rapid prototyping, and allows engineers to create complex geometric '
             'shapes that cannot be made with traditional molds. This exposure teaches students basic CAD '
             'principles and empowers them to turn their own digital ideas into tangible inventions.',
  'duration': '15–20 min',
  'icon': '🖨️',
  'short': '3D Printing, formally known as additive manufacturing, is the process of creating solid '
           'three-dimensional physical objects from a digital Computer-Aided Design (CAD) file. Unlike '
           'traditional subtractive manufacturing—which cuts or drills material away from a solid block—3D '
           'printing builds objects layer by layer from the bottom up.',
  'title': '3D Printing (Additive Manufacturing)'},
 {'age': 'Classes 7–12',
  'details': 'Drone Technology involves the design, flight mechanics, navigation, and practical operation of '
             'Unmanned Aerial Vehicles (UAVs) controlled either remotely by a pilot or autonomously via '
             'onboard computers. Inside the Technology on Wheels bus, students examine the anatomy of '
             'multi-rotor drones, including brushless motors, electronic speed controllers (ESCs), flight '
             'controllers, lithium-polymer batteries, and GPS modules. Demonstrations explain the physics of '
             'flight, showing how varying the rotational speed of propellers controls pitch, roll, yaw, and '
             'altitude. A major focus of the module is on agricultural drones, which are transforming '
             'farming in Maharashtra by spraying fertilizers and pesticides evenly while saving water and '
             'protecting farmers from chemical exposure. Students also learn how drones equipped with '
             'high-resolution and multispectral cameras conduct land surveying, crop health mapping, and '
             'disaster relief monitoring. Safety regulations, no-fly zones, and basic flight simulator '
             'controls are also introduced. By exploring UAV systems, students see how aerodynamics, '
             'sensors, and software come together to solve real-world rural and industrial challenges.',
  'duration': '15–25 min',
  'icon': '🚁',
  'short': 'Drone Technology involves the design, flight mechanics, navigation, and practical operation of '
           'Unmanned Aerial Vehicles (UAVs) controlled either remotely by a pilot or autonomously via '
           'onboard computers. Inside the Technology on Wheels bus, students examine the anatomy of '
           'multi-rotor drones, including brushless motors, electronic speed controllers (ESCs), flight '
           'controllers, lithium-polymer batteries, and GPS modules.',
  'title': 'Drone Technology (Unmanned Aerial Vehicles)'}]
ABOUT_FULL = ('The Technology on Wheels bus is an innovative mobile educational laboratory launched by Vidya '
 'Pratishthan’s Sharadchandra Pawar Centre of Excellence in Artificial Intelligence (VPSPCOE) in '
 'collaboration with the Sakal Media Group. Inaugurated in June 2026 by Sharad Pawar alongside Supriya Sule '
 'and Prataprao Pawar, this specially designed robotic bus brings advanced technological education directly '
 'to students in rural and remote areas. Rather than serving as a simple display, the vehicle functions as '
 'an interactive mobile technology center. Inside the bus, students can explore live working models and '
 'hands-on demonstrations focused on Artificial Intelligence (AI), Robotics, and Augmented Reality (AR). One '
 'of its standout attractions is an onboard interactive robot that greets visitors and explains the various '
 'systems and exhibits to the students. By traveling directly to schools across different regions, the '
 'initiative removes geographical and financial barriers that often limit rural students from accessing '
 'modern STEM infrastructure. The program aims to spark early curiosity, promote digital literacy, and make '
 'complex emerging technologies easy to understand through practical, visual learning. Ultimately, the '
 'Technology on Wheels bus empowers thousands of young learners with future-ready skills and inspires them '
 'to pursue careers in science, engineering, and artificial intelligence.')
VISION = ('The Technology on Wheels bus is a mobile education initiative launched by Vidya Pratishthan’s '
 'Sharadchandra Pawar Centre of Excellence in AI (VPSPCOE) in collaboration with the Sakal Media Group. Its '
 'core vision is to bridge the digital divide by bringing cutting-edge technologies like Artificial '
 'Intelligence, Robotics, and Augmented Reality directly to students in rural and remote areas. Functioning '
 'as a state-of-the-art mobile technology center rather than a simple exhibition, the bus features '
 'interactive models, live demonstrations, and even an onboard robot guide to make complex concepts '
 'accessible. By delivering hands-on exposure to thousands of school students at their doorstep, the project '
 'aims to spark early scientific curiosity and modernize rural education. Ultimately, this initiative seeks '
 'to democratize tech literacy and prepare the next generation of students from underserved regions for a '
 'rapidly evolving digital future.')
MISSION_INTRO = ('The Technology on Wheels bus is a mobile education initiative launched by Vidya Pratishthan’s '
 'Sharadchandra Pawar Centre of Excellence in Artificial Intelligence (VPSPCOE-AI) in collaboration with the '
 'Sakal Media Group.')
MISSION_POINTS = [('Rural Outreach',
  'It aims to bring cutting-edge technological education directly to students in rural and remote areas.'),
 ('Modern Tech Exposure',
  'The mobile unit introduces school students to advanced fields like Artificial Intelligence (AI), '
  'Robotics, and Augmented Reality (AR).'),
 ('Interactive Learning',
  'It operates as a traveling technology center equipped with live working models and hands-on '
  'demonstrations rather than a passive exhibition.'),
 ('AI-Guided Demonstrations',
  'The bus features an onboard interactive robot designed to explain complex technological concepts directly '
  'to visiting students.'),
 ('Bridging the Digital Divide',
  'Inaugurated in June 2026 in Pune, the mission strives to make modern, interactive digital learning '
  'accessible to thousands of underserved students.')]
TEAM = [('Mulik Aditya Sharad', '25102033', 'EN25102033'),
 ('Mahajan Shivam Sambha', '25102030', 'EN25102030'),
 ('Nalawade Shreya Arvind', '25142034', 'EN25142034'),
 ('Nimbalkar Arati Dipak', '25102040', 'EN25102040')]