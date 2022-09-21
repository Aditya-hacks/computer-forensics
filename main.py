<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <title>Cyber Forensics Computing</title>
    
</head>
<body

  x-data="{navOpen: false, scrolledFromTop: false}"
      x-init="window.pageYOffset >= 50 ? scrolledFromTop = true : scrolledFromTop = false"
      @scroll.window="window.pageYOffset >= 50 ? scrolledFromTop = true : scrolledFromTop = false"
      :class="{
      'overflow-hidden': navOpen,
      'overflow-scroll': !navOpen
      }"
   >
      <header
         class="
            fixed
            w-full
            bg-blue-500
            flex
            justify-between
            items-center
            px-4
            md:px-12
            transition-all
            duration-200
            h-24
         "
         :class="{'h-24': !scrolledFromTop, 'h-14': scrolledFromTop}"
      >
         <a href="#">
            

            <img
               src="image/cccc.png"
               
               
               alt="Logo"
               class="h-20 transform origin-left transition duration-200"
               :class="{'scale-100': !scrolledFromTop, 'scale-75': scrolledFromTop}"
            />
         </a>
         <nav>
            <button class="md:hidden" @click="navOpen = !navOpen">
               <svg
                  xmlns="http://www.w3.org/2000/svg"
                  class="h-8 w-8 text-white"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke="currentColor"
               >
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
               </svg>
            </button>
            <ul
               class="
                  fixed
                  left-0
                  right-0
                  min-h-screen
                  px-4
                  pt-8
                  space-y-4
                  bg-blue-500
                  text-white
                  transform
                  transition
                  duration-300
                  translate-x-full
                  md:relative md:flex md:space-x-10 md:min-h-0 md:px-0 md:py-0 md:space-y-0 md:translate-x-0
               "
               :class="{'translate-x-full': !navOpen}"
               :class="{'translate-x-0': navOpen}"
            >
               
               <li class="">
                  <a href="#Home" @click="navOpen = false">Home</a>
               </li>
               <li class="">
                  <a href="#Tutorials" @click="navOpen = false">Tutorials</a>
               </li>
               <li>
                  <a href="#Projects" @click="navOpen = false">Projects</a>
               </li>
               <li>
                  <a href="#Contact Us" @click="navOpen = false">Contact Us</a>
               </li>
               
            </ul>
         </nav>
      </header>

      <header class="text-gray-600 body-font">
        <div class="container mx-auto flex flex-wrap p-5 flex-col md:flex-row items-center">
          
          <nav class="md:ml-auto md:mr-auto flex flex-wrap items-center text-base justify-center">
            <a href="#home" class="mr-5 hover:text-gray-900"></a>
            <a href="Tutorials" class="mr-5 hover:text-gray-900"></a>
            <a href="Projects" class="mr-5 hover:text-gray-900"></a>
            <a href="Contact Us" class="mr-5 hover:text-gray-900"></a>
          </nav>
        </div>
      </header>     
          
        

      <hr>

      
      
      <section class="text-gray-600 body-font">
        <div class="container mx-auto flex px-5 py-24 md:flex-row flex-col items-center">
          <div class="lg:flex-grow md:w-1/2 lg:pr-24 md:pr-16 flex flex-col md:items-start md:text-left mb-16 md:mb-0 items-center text-center">
            <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">What is Digital Forensics?
              
            </h1>
            <p class="mb-8 leading-relaxed">Digital Forensics is the retrieval, analysis, and use of digital evidence in a civil or criminal investigation. Ironically, digital forensics (or computer forensics) is not limited to computers as the source of evidence. Any medium that can store digital files is a potential source of evidence for a computer forensics investigator. Therefore, digital forensics involves the examination of digital files.  Digital forensics is a science because of the accepted practices used for acquiring and examining the evidence and its admissibility in court. Additionally, the tools used to retrieve and analyze digital evidence have been subjected to scientific testing over many years. In fact, the word forensics means “suitable for a court of law”. This definition infers that digital evidence used in an investigation needs to be retrieved, handled, and analyzed in a forensically sound manner. Forensically sound means that, during the acquisition of digital evidence and throughout the investigative process, the evidence must remain in its original state. Moreover, everyone who has been in contact with the evidence must be accounted for and documented in the chain of custody form. </p>
            <div class="flex justify-center">

              
            </div>
          </div>
          <div class="lg:max-w-lg lg:w-full md:w-1/2 w-5/6">
            <img class="object-cover object-center rounded" alt="hero" src="https://www.eccu.edu/wp-content/uploads/2020/01/Digital-Forensics.jpg">
          </div>
        </div>
      </section>
      <hr>
      <section class="text-gray-600 body-font">
        <div class="container mx-auto flex px-5 py-24 md:flex-row flex-col items-center">
          <div class="lg:max-w-lg lg:w-full md:w-1/2 w-5/6 mb-10 md:mb-0">
            <img class="object-cover object-center rounded" alt="hero" src="https://cutewallpaper.org/21/forensics-wallpaper/Endpoint-Forensics-Ingalls-Information-Security.jpg">
          </div>
          <div class="lg:flex-grow md:w-1/2 lg:pl-24 md:pl-16 flex flex-col md:items-start md:text-left items-center text-center">
            <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">Importance of Digital Forensics
              
            </h1>
            <p class="mb-8 leading-relaxed">In the civil and criminal justice system, computer forensics helps ensure the integrity of digital evidence presented in court cases. As computers and other data-collecting devices are used more frequently in every aspect of life, digital evidence -- and the forensic process used to collect, preserve and investigate it -- has become more important in solving crimes and other legal issues. The average person never sees much of the information modern devices collect. For instance, the computers in cars continually collect information on when a driver brakes, shifts and changes speed without the driver being aware. However, this information can prove critical in solving a legal matter or a crime, and computer forensics often plays a role in identifying and preserving that information. </p>
            <div class="flex justify-center">
              
            </div>
          </div>
        </div>
      </section>

      
      <hr>
      
      <div class="text-center mb-20">
        <h1 class="sm:text-3xl text-2xl font-medium text-center title-font text-gray-900 mb-4">Steps involved in Digital Forensics</h1>
        
      </div>
      <section class="text-gray-600 body-font">
        <div class="container px-5 py-24 mx-auto flex flex-wrap">
          <div class="flex flex-wrap w-full">
            <div class="lg:w-2/5 md:w-1/2 md:pr-10 md:py-6">
              <div class="flex relative pb-12">
                <div class="h-full w-10 absolute inset-0 flex items-center justify-center">
                  <div class="h-full w-1 bg-gray-200 pointer-events-none"></div>
                </div>
                <div class="flex-shrink-0 w-10 h-10 rounded-full bg-indigo-500 inline-flex items-center justify-center text-white relative z-10">
                  <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                  </svg>
                </div>
                <div class="flex-grow pl-4">
                  <h2 class="font-medium title-font text-sm text-gray-900 mb-1 tracking-wider">Identification</h2>
                  <p class="leading-relaxed">First, find the evidence, noting where it is stored.</p>
                </div>
              </div>
              <div class="flex relative pb-12">
                <div class="h-full w-10 absolute inset-0 flex items-center justify-center">
                  <div class="h-full w-1 bg-gray-200 pointer-events-none"></div>
                </div>
                <div class="flex-shrink-0 w-10 h-10 rounded-full bg-indigo-500 inline-flex items-center justify-center text-white relative z-10">
                  <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                    <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
                  </svg>
                </div>
                <div class="flex-grow pl-4">
                  <h2 class="font-medium title-font text-sm text-gray-900 mb-1 tracking-wider">Preservation</h2>
                  <p class="leading-relaxed">Next, isolate, secure, and preserve the data. This includes preventing people from possibly tampering with the evidence.</p>
                </div>
              </div>
              <div class="flex relative pb-12">
                <div class="h-full w-10 absolute inset-0 flex items-center justify-center">
                  <div class="h-full w-1 bg-gray-200 pointer-events-none"></div>
                </div>
                <div class="flex-shrink-0 w-10 h-10 rounded-full bg-indigo-500 inline-flex items-center justify-center text-white relative z-10">
                  <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                    <circle cx="12" cy="5" r="3"></circle>
                    <path d="M12 22V8M5 12H2a10 10 0 0020 0h-3"></path>
                  </svg>
                </div>
                <div class="flex-grow pl-4">
                  <h2 class="font-medium title-font text-sm text-gray-900 mb-1 tracking-wider">Analysis</h2>
                  <p class="leading-relaxed">Next, reconstruct fragments of data and draw conclusions based on the evidence found.</p>
                </div>
              </div>
              <div class="flex relative pb-12">
                <div class="h-full w-10 absolute inset-0 flex items-center justify-center">
                  <div class="h-full w-1 bg-gray-200 pointer-events-none"></div>
                </div>
                <div class="flex-shrink-0 w-10 h-10 rounded-full bg-indigo-500 inline-flex items-center justify-center text-white relative z-10">
                  <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                    <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"></path>
                    <circle cx="12" cy="7" r="4"></circle>
                  </svg>
                </div>
                <div class="flex-grow pl-4">
                  <h2 class="font-medium title-font text-sm text-gray-900 mb-1 tracking-wider">Documentation</h2>
                  <p class="leading-relaxed">Following that, create a record of all the data to recreate the crime scene.</p>
                </div>
              </div>
              <div class="flex relative">
                <div class="flex-shrink-0 w-10 h-10 rounded-full bg-indigo-500 inline-flex items-center justify-center text-white relative z-10">
                  <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="w-5 h-5" viewBox="0 0 24 24">
                    <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
                    <path d="M22 4L12 14.01l-3-3"></path>
                  </svg>
                </div>
                <div class="flex-grow pl-4">
                  <h2 class="font-medium title-font text-sm text-gray-900 mb-1 tracking-wider">Presentation</h2>
                  <p class="leading-relaxed">Lastly, summarize and draw a conclusion.</p>
                </div>
              </div>
            </div>
            <img class="lg:w-3/5 md:w-1/2 object-cover object-center rounded-lg md:mt-0 mt-12" src="https://cdn.educba.com/academy/wp-content/uploads/2020/06/Process-of-Digital-Forensics.jpg" alt="step">
          </div>
        </div>
      </section>
      <hr>

      <section class="text-gray-600 body-font">
        <div class="container px-5 py-24 mx-auto">
          <div class="text-center mb-20">
            <h1 class="sm:text-3xl text-2xl font-medium text-center title-font text-gray-900 mb-4">Phases Of Digital Forensics</h1>
            <p class="text-base leading-relaxed xl:w-2/4 lg:w-3/4 mx-auto">Phases involved in Digital Forensics are: </p>
          </div>
          <div class="flex flex-wrap lg:w-4/5 sm:mx-auto sm:mb-2 -mx-2">
            <div class="p-2 sm:w-1/2 w-full">
              <div class="bg-gray-100 rounded flex p-4 h-full items-center">
                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-indigo-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
                  <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
                  <path d="M22 4L12 14.01l-3-3"></path>
                </svg>
                <span class="title-font font-medium">First Response</span>
              </div>
            </div>
            <div class="p-2 sm:w-1/2 w-full">
              <div class="bg-gray-100 rounded flex p-4 h-full items-center">
                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-indigo-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
                  <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
                  <path d="M22 4L12 14.01l-3-3"></path>
                </svg>
                <span class="title-font font-medium">Search and Seizure</span>
              </div>
            </div>
            <div class="p-2 sm:w-1/2 w-full">
              <div class="bg-gray-100 rounded flex p-4 h-full items-center">
                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-indigo-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
                  <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
                  <path d="M22 4L12 14.01l-3-3"></path>
                </svg>
                <span class="title-font font-medium">Collect the Evidence</span>
              </div>
            </div>
            <div class="p-2 sm:w-1/2 w-full">
              <div class="bg-gray-100 rounded flex p-4 h-full items-center">
                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-indigo-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
                  <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
                  <path d="M22 4L12 14.01l-3-3"></path>
                </svg>
                <span class="title-font font-medium">Secure the Evidence</span>
              </div>
            </div>
            <div class="p-2 sm:w-1/2 w-full">
              <div class="bg-gray-100 rounded flex p-4 h-full items-center">
                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-indigo-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
                  <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
                  <path d="M22 4L12 14.01l-3-3"></path>
                </svg>
                <span class="title-font font-medium">Data Acquisition</span>
              </div>
            </div>
            <div class="p-2 sm:w-1/2 w-full">
              <div class="bg-gray-100 rounded flex p-4 h-full items-center">
                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-indigo-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
                  <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
                  <path d="M22 4L12 14.01l-3-3"></path>
                </svg>
                <span class="title-font font-medium">Data Analysis</span>
              </div>
            </div>
            <div class="p-2 sm:w-1/2 w-full">
              <div class="bg-gray-100 rounded flex p-4 h-full items-center">
                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-indigo-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
                  <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
                  <path d="M22 4L12 14.01l-3-3"></path>
                </svg>
                <span class="title-font font-medium">Evidence Assessment</span>
              </div>
            </div>
            <div class="p-2 sm:w-1/2 w-full">
              <div class="bg-gray-100 rounded flex p-4 h-full items-center">
                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-indigo-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
                  <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
                  <path d="M22 4L12 14.01l-3-3"></path>
                </svg>
                <span class="title-font font-medium">Documentation and Reporting</span>
              </div>
            </div>
            <div class="p-2 sm:w-1/2 w-full">
              <div class="bg-gray-100 rounded flex p-4 h-full items-center">
                <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="3" class="text-indigo-500 w-6 h-6 flex-shrink-0 mr-4" viewBox="0 0 24 24">
                  <path d="M22 11.08V12a10 10 0 11-5.93-9.14"></path>
                  <path d="M22 4L12 14.01l-3-3"></path>
                </svg>
                <span class="title-font font-medium">Testify as an Expert Witness</span>
              </div>
            </div>


          </div>
          
        </div>
      </section>
      <hr>


      
      <section class="text-gray-600 body-font">
        
        <div class="container px-5 py-24 mx-auto">
          <div class="text-center mb-20">
            <h1 class="sm:text-3xl text-2xl font-medium text-center title-font text-gray-900 mb-4">Roles Of Digital Forensics Investigator</h1>
            
          </div>
          
          <div class="flex items-center lg:w-3/5 mx-auto border-b pb-10 mb-10 border-gray-200 sm:flex-row flex-col">
            <div class="sm:w-32 sm:h-32 h-20 w-20 sm:mr-10 inline-flex items-center justify-center rounded-full bg-indigo-100 text-indigo-500 flex-shrink-0">
              
              <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="sm:w-16 sm:h-16 w-10 h-10" viewBox="0 0 24 24">
                <path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>
              </svg>
              
            </div>
            
            <div class="flex-grow sm:text-left text-center mt-6 sm:mt-0">
              <h2 class="text-gray-900 text-lg title-font font-medium mb-2">First Responder</h2>
              <p class="leading-relaxed text-base">This role is responsible for the initiation of the digital investigation, securing the scene of the incident, primary identification of the digital evidence, securing the evidence, and identifying the digital investigation procedures that should be followed for the specific type of incident. These roles might also be part of the incident response team or security operations center (SOC).</p>
              
                
              
            </div>
          </div>
          <div class="flex items-center lg:w-3/5 mx-auto border-b pb-10 mb-10 border-gray-200 sm:flex-row flex-col">
            <div class="flex-grow sm:text-left text-center mt-6 sm:mt-0">
              <h2 class="text-gray-900 text-lg title-font font-medium mb-2">Digital Forensics Specialist</h2>
              <p class="leading-relaxed text-base">This role is responsible for identification and collection of the digital evidence ensuring the forensic principles are followed. This role can have a responsibility to perform live forensics.</p>
              
            </div>
            <div class="sm:w-32 sm:order-none order-first sm:h-32 h-20 w-20 sm:ml-10 inline-flex items-center justify-center rounded-full bg-indigo-100 text-indigo-500 flex-shrink-0">
              <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="sm:w-16 sm:h-16 w-10 h-10" viewBox="0 0 24 24">
                <circle cx="6" cy="6" r="3"></circle>
                <circle cx="6" cy="18" r="3"></circle>
                <path d="M20 4L8.12 15.88M14.47 14.48L20 20M8.12 8.12L12 12"></path>
              </svg>
            </div>
          </div>
          <div class="flex items-center lg:w-3/5 mx-auto sm:flex-row flex-col">
            <div class="sm:w-32 sm:h-32 h-20 w-20 sm:mr-10 inline-flex items-center justify-center rounded-full bg-indigo-100 text-indigo-500 flex-shrink-0">
              <svg fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="sm:w-16 sm:h-16 w-10 h-10" viewBox="0 0 24 24">
                <path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"></path>
                <circle cx="12" cy="7" r="4"></circle>
              </svg>
            </div>
            <div class="flex-grow sm:text-left text-center mt-6 sm:mt-0">
              <h2 class="text-gray-900 text-lg title-font font-medium mb-2">Digital Forensics Analyst/Examiner</h2>
              <p class="leading-relaxed text-base">This role is responsible for analysis of different types of digital evidence and reporting the results. This role can also have a responsibility for performing live forensics.</p>
              
            </div>
            
             
          </div>
        </div>

        
      </section>

      <hr>

      <section class="text-gray-600 body-font">
        <div class="container px-5 py-24 mx-auto">
          <div class="flex flex-col text-center w-full mb-20">
            <h1 class="text-2xl font-medium title-font mb-4 text-gray-900">OUR TEAM</h1>
          </div>
          <div class="flex flex-wrap -m-4">
            <div class="p-4 lg:w-1/4 md:w-1/2">
              <div class="h-full flex flex-col items-center text-center">
                <div class="team"><img src="image/sai.jpg" alt="team"></div>
                <div class="w-full">
                  <h2 class="title-font font-medium text-lg text-gray-900">Varayogula Sai Niveditha</h2>
                  <h3 class="text-gray-500 mb-3">Practical forensics tools videos .</h3>
                  
                </div>
              </div>
            </div>
            <div class="p-4 lg:w-1/4 md:w-1/2">
              <div class="h-full flex flex-col items-center text-center">
                <div class="team"><img src="image/ishika.jpg" alt="team"></div>
                <div class="w-full">
                  <h2 class="title-font font-medium text-lg text-gray-900">Ishika Goel</h2>
                  <h3 class="text-gray-500 mb-3">Project demonstration.</h3>
                  
                </div>
              </div>
            </div>
            <div class="p-4 lg:w-1/4 md:w-1/2">
              <div class="h-full flex flex-col items-center text-center">
                <div class="team"><img src="image/adi.jpg" alt="team"></div>
                <div class="w-full">
                  <h2 class="title-font font-medium text-lg text-gray-900">Aditya Agarwal</h2>
                  <h3 class="text-gray-500 mb-3">Project demonstartion.</h3>
                  
                </div>
              </div>
            </div>
            
          </div>
        </div>
      </section>
      
<hr>

      

<!--          tutorial section           -->

<section class="text-gray-600 body-font">
  <div class="container px-5 py-24 mx-auto">
    <div class="flex flex-wrap -mx-4 -mb-10 text-center">
      <div class="sm:w-1/2 mb-10 px-4">
        <div class="rounded-lg h-64 overflow-hidden">
          <a href="https://www.youtube.com/channel/UCWqOsQ5MW5fujDx5uwi6hsw">
          <img alt="content" class="object-cover object-center h-full w-full" src="image/Autopsy.png">
        </a>
        </div>
        <h2 class="title-font text-2xl font-medium text-gray-900 mt-6 mb-3">Autopsy</h2>
        <p class="leading-relaxed text-base">Autopsy® is a digital forensics platform and graphical interface to The Sleuth Kit® and other digital forensics tools. It is used by law enforcement, military, and corporate examiners to investigate what happened on a computer. You can even use it to recover photos from your camera’s memory card.</p>
        <a href="   ">
        <button class="flex mx-auto mt-6 text-white bg-indigo-500 border-0 py-2 px-5 focus:outline-none hover:bg-indigo-600 rounded">Play</button>
        </a>
      </div>
      <div class="sm:w-1/2 mb-10 px-4">
        <div class="rounded-lg h-64 overflow-hidden">
          <a href="https://youtu.be/2RrAj69bYA8">
          <img alt="content" class="object-cover object-center h-full w-full" src="image/FTK.png">
        </a>
        </div>
        <h2 class="title-font text-2xl font-medium text-gray-900 mt-6 mb-3">FTK Imager</h2>
        <p class="leading-relaxed text-base">FTK Imager is an open-source software by AccessData that is used for creating accurate copies of the original evidence without actually making any changes to it. The Image of the original evidence is remaining the same and allows us to copy data at a much faster rate, which can be soon be preserved and can be analyzed further.</p>
        <a href="https://www.youtube.com/watch?v=2RrAj69bYA8&t=107s">
        <button class="flex mx-auto mt-6 text-white bg-indigo-500 border-0 py-2 px-5 focus:outline-none hover:bg-indigo-600 rounded">Play</button>
        </a>
      </div>
    </div>
  </div>
</section>


<section class="text-gray-600 body-font">
  <div class="container px-5 py-24 mx-auto">
    <div class="flex flex-wrap -mx-4 -mb-10 text-center">
      <div class="sm:w-1/2 mb-10 px-4">
        <div class="rounded-lg h-64 overflow-hidden">
          <a href="https://youtu.be/6jIAtiWjjk0">
          <img alt="content" class="object-cover object-center h-full w-full" src="image/Volatility.png">
          </a>
        </div>
        <h2 class="title-font text-2xl font-medium text-gray-900 mt-6 mb-3">Volatility</h2>
        <p class="leading-relaxed text-base">Volatility is the open source software programs for analyzing RAM in 32 bit/64 bit systems. It can analyze raw dumps, crash dumps, VMware dumps (.vmem), virtual box dumps, and many others.</p>
        <a href="https://youtu.be/6jIAtiWjjk0">
        <button class="flex mx-auto mt-6 text-white bg-indigo-500 border-0 py-2 px-5 focus:outline-none hover:bg-indigo-600 rounded">Play</button>
        </a>
      </div>
      <div class="sm:w-1/2 mb-10 px-4">
        <div class="rounded-lg h-64 overflow-hidden">
          <a href="https://youtu.be/WhQ10MN9WCc">
          <img alt="content" class="object-cover object-center h-full w-full" src="image/Stegano.png">
          </a>
        </div>
        <h2 class="title-font text-2xl font-medium text-gray-900 mt-6 mb-3">Image Steganography</h2>
        <p class="leading-relaxed text-base">Steganography is the study and practice of concealing information within objects in such a way that it deceives the viewer as if there is no information hidden within the object. Simply put, it is hiding information in plain sight, such that only the intended recipient would get to see it.</p>
        <a href="https://youtu.be/WhQ10MN9WCc">
        <button class="flex mx-auto mt-6 text-white bg-indigo-500 border-0 py-2 px-5 focus:outline-none hover:bg-indigo-600 rounded">Play</button>
        </a>
      </div>
    </div>
  </div>
</section>

<section class="text-gray-600 body-font">
  <div class="container px-5 py-24 mx-auto">
    <div class="flex flex-wrap -mx-4 -mb-10 text-center">
      <div class="sm:w-1/2 mb-10 px-4">
        <div class="rounded-lg h-64 overflow-hidden">
          <img alt="content" class="object-cover object-center h-full w-full" src="image/exif.png">
        </div>
        <h2 class="title-font text-2xl font-medium text-gray-900 mt-6 mb-3">Exif Tool</h2>
        <p class="leading-relaxed text-base">ExifTool is a free and open-source software program for reading, writing, and manipulating image, audio, video, and PDF metadata.</p>
        <a href="https://drive.google.com/file/d/1z-X1ZPPp6wY762PV_EDhNQx-gCQXsoV4/view?usp=sharing">
        <button class="flex mx-auto mt-6 text-white bg-indigo-500 border-0 py-2 px-5 focus:outline-none hover:bg-indigo-600 rounded">Play</button>
      </a>
      </div>
      <div class="sm:w-1/2 mb-10 px-4">
        <div class="rounded-lg h-64 overflow-hidden">
          <img alt="content" class="object-cover object-center h-full w-full" src="image/bulk.png">
        </div>
        <h2 class="title-font text-2xl font-medium text-gray-900 mt-6 mb-3">Bulk Extractor</h2>
        <p class="leading-relaxed text-base">It scans a disk image, a file, or a directory of files and extracts useful information without parsing the file system or file system structures.</p>
        <a href="https://drive.google.com/file/d/1WgZ1A7OwmF1t3KsZDsUCUW8xwSy6knfS/view?usp=sharing">
        <button class="flex mx-auto mt-6 text-white bg-indigo-500 border-0 py-2 px-5 focus:outline-none hover:bg-indigo-600 rounded">Play</button>
        </a>
      </div>
    </div>
  </div>
</section>



<section class="text-gray-600 body-font">
  <div class="container px-5 py-24 mx-auto">
    <div class="flex flex-wrap -mx-4 -mb-10 text-center">
<div class="sm:w-1/2 mb-10 px-4">
  <div class="rounded-lg h-64 overflow-hidden">
    <a href="https://youtu.be/6jIAtiWjjk0">
    <img alt="content" class="object-cover object-center h-full w-full" src="image/usb.png">
    </a>
  </div>
  <h2 class="title-font text-2xl font-medium text-gray-900 mt-6 mb-3">USB Detective </h2>
  <p class="leading-relaxed text-base">USB Detective aims to ease the burden on the examiner by visually distinguishing attributes with inconsistent timestamps from those with multiple corroborating sources.</p>
  <a href="https://drive.google.com/file/d/194OSc5ByRIVGGyAFQb90dcXV-uTQ0BQY/view?usp=sharing">
  <button class="flex mx-auto mt-6 text-white bg-indigo-500 border-0 py-2 px-5 focus:outline-none hover:bg-indigo-600 rounded">Play</button>
  </a>
</div>
<div class="sm:w-1/2 mb-10 px-4">
  <div class="rounded-lg h-64 overflow-hidden">
    <img alt="content" class="object-cover object-center h-full w-full" src="image/wra.png">
  </div>
  <h2 class="title-font text-2xl font-medium text-gray-900 mt-6 mb-3">Windows Registry Analysis</h2>
  <p class="leading-relaxed text-base">The Registry is a various levelled or we can say a hierarchical database that stores low-level settings and other information for the Microsoft Windows Operating System and for applications that pick to utilize the registry.</p>
  <a href="https://drive.google.com/file/d/1oGOBu8JC49D6km89FzDYpTw6E0wnzam5/view?usp=sharing">
  <button class="flex mx-auto mt-6 text-white bg-indigo-500 border-0 py-2 px-5 focus:outline-none hover:bg-indigo-600 rounded">Play</button>
  </a>
</div>
</div>
</div>
</section>


<section class="text-gray-600 body-font">
  <div class="container px-5 py-24 mx-auto">
    <div class="flex flex-wrap -mx-4 -mb-10 text-center">
      <div class="sm:w-1/2 mb-10 px-4">
        <div class="rounded-lg h-64 overflow-hidden">
          <img alt="content" class="object-cover object-center h-full w-full" src="image/pfa.png">
        </div>
        <h2 class="title-font text-2xl font-medium text-gray-900 mt-6 mb-3">Prefetch File Analysis</h2>
        <p class="leading-relaxed text-base">Prefetch files are great artifacts for forensic investigators trying to analyze applications that have been run on a system. Windows creates a prefetch file when an application is run from a particular location for the very first time. This is used to help speed up the loading of applications.</p>
        <a href="https://drive.google.com/file/d/1FQlFHFIYPg9OFcJ7Ss8a-coCE_bZHvY3/view?usp=sharing">
        <button class="flex mx-auto mt-6 text-white bg-indigo-500 border-0 py-2 px-5 focus:outline-none hover:bg-indigo-600 rounded">Play</button>
        </a>
      </div>
      <div class="sm:w-1/2 mb-10 px-4">
        <div class="rounded-lg h-64 overflow-hidden">
          <img alt="content" class="object-cover object-center h-full w-full" src="image/shell.png">
        </div>
        <h2 class="title-font text-2xl font-medium text-gray-900 mt-6 mb-3">Shellbags Analysis</h2>
        <p class="leading-relaxed text-base">Shellbags are set of registry keys which contain details about a user’s viewed folder; such as its size, position, and icon. This means that all directory traversal is tracked and maintained in the registry.</p>
        <a href="https://drive.google.com/file/d/1YxgSQhFPJslBQsWKqChdmCylVH-0gPha/view?usp=sharing">
        <button class="flex mx-auto mt-6 text-white bg-indigo-500 border-0 py-2 px-5 focus:outline-none hover:bg-indigo-600 rounded">Play</button>
        </a>
      </div>
    </div>
  </div>
</section>

<hr>

<section class="text-gray-600 body-font">
  <div class="container mx-auto flex px-5 py-24 items-center justify-center flex-col">
    <img class="lg:w-2/6 md:w-3/6 w-5/6 mb-10 object-cover object-center rounded" alt="hero" src="image/cybersof.png">
    <div class="text-center lg:w-2/3 w-full">
      <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">Crime Investigation Software</h1>
      <p class="mb-8 leading-relaxed"></p>
      <a href="https://drive.google.com/file/d/1TfLZS4bVTdSLuHApSOdmXvDQGCM5SdL8/view?usp=sharing">
      <div class="flex justify-center">
        <button class="inline-flex text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg">Download</button>
      </a>
      </div>
    </div>
  </div>
</section>


<section class="text-gray-600 body-font">
  <div class="container mx-auto flex px-5 py-24 items-center justify-center flex-col">
    <img class="lg:w-2/6 md:w-3/6 w-5/6 mb-10 object-cover object-center rounded" alt="hero" src="image/credit.png">
    <div class="text-center lg:w-2/3 w-full">
      <h1 class="title-font sm:text-4xl text-3xl mb-4 font-medium text-gray-900">Credit Card Fraud Detection</h1>
      <p class="mb-8 leading-relaxed"></p>
      <a href="https://drive.google.com/file/d/19Itpkw-A4mwlPb9ktKqSRScd-wrcwnEG/view?usp=sharing">
      <div class="flex justify-center">
        <button class="inline-flex text-white bg-indigo-500 border-0 py-2 px-6 focus:outline-none hover:bg-indigo-600 rounded text-lg">Download</button>
      </a>
      </div>
    </div>
  </div>


</section>

<hr>


<section class="text-gray-600 body-font relative">
  <div class="container px-5 py-24 mx-auto">
    <div class="flex flex-col text-center w-full mb-12">
      <h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">Contact Us</h1>
      <p class="lg:w-2/3 mx-auto leading-relaxed text-base">Feel free to contact us.</p>
    </div>
    <div class="lg:w-1/2 md:w-2/3 mx-auto">
      <div class="flex flex-wrap -m-2">
        <div class="p-2 w-1/2">
          <div class="relative">
            <label for="name" class="leading-7 text-sm text-gray-600">Name</label>
            <input type="text" id="name" name="name" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
          </div>
        </div>
        <div class="p-2 w-1/2">
          <div class="relative">
            <label for="email" class="leading-7 text-sm text-gray-600">Email</label>
            <input type="email" id="email" name="email" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out">
          </div>
        </div>
        <div class="p-2 w-full">
          <div class="relative">
            <label for="message" class="leading-7 text-sm text-gray-600">Message</label>
            <textarea id="message" name="message" class="w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 h-32 text-base outline-none text-gray-700 py-1 px-3 resize-none leading-6 transition-colors duration-200 ease-in-out"></textarea>
          </div>
        </div>
        <div class="p-2 w-full">
          <button class="flex mx-auto text-white bg-indigo-500 border-0 py-2 px-8 focus:outline-none hover:bg-indigo-600 rounded text-lg">Send</button>
        </div>
        <div class="p-2 w-full pt-8 mt-8 border-t border-gray-200 text-center">
          
          
          
        </div>
      </div>
    </div>
  </div>
</section>

</body>
</html>
