import time
"Abhilash Rajeshwaran"	"Sr. Faculty-  Visual Effects & Animation and Game Art & Design" 
l = [
"Abhilash-Rajeshwaran.jpg",
"Abid-Shaikh.jpg",
"Aditya-Havile.jpg",
"Ajay-Thomas.jpg",
"Alok-Katkar.jpg",
"Anoop-Chaphekar.jpg",
"Arindam-Das.jpg",
"Arun-Gupta.jpg",
"Ayush-Chaudhary.jpg",
"Chandan-Sirish.jpg",
"Deep-Achtani.jpg",
"Deivendra-Kumar.jpg",
"Dinesh-Bhatlavande.jpg",
"Dinesh-Khemani.jpg",
"Hritik-Mahirao.jpg",
"Jaikishan-SG.jpg",
"Jayprakash-Sahu.jpg",
"Jijin-PK.jpg",
"Johnston-DSouza.jpg",
"Kamal-Srivastava.jpg",
"Kartikeya-Dixit.jpg",
"Ketan-Deshpande.jpg",
"Krishna-Aditya.jpg",
"Manasi-Raut.jpg",
"Mandar-Patil.jpg",
"Mohamed-Rafi.jpg",
"Mohanish-Deshmukh.jpg",
"Mohd-Wajahatulla-Naseem.jpg",
"Nikhil-Bejai.jpg",
"Prabat-Ranjan.jpg",
"Prathviraj.jpg",
"Purva-Gadre.jpg",
"Rahul-Singh.jpg",
"Ravi-Singh.jpg",
"Sachin-Chandane.jpg",
"Salil-Upadhyay.jpg",
"Sanjita-Shetye.jpg",
"Saurabh-Mishra.jpg",
"Shiva-Gupta.jpg",
"Shoeb-Khan.jpg",
"Sneha-Sonawane.jpg",
"Snigdhadeep-Nag.jpg",
"Sreekumar-Unnithan.jpg",
"Sukhada-Khandge.jpg",
"Sunil-Kumar-K.jpg",
"Sunkeerthi.jpg",
"Supreel-Gharat.jpg",
"Sushant-Kulkarni.jpg",
"Suvedha.jpg",
"Tanmoy-Datta.jpg",
"Varsha-Dongre.jpg",
"Ved-Verma.jpg",
]

file = open("file.txt", "w")
for i in l:
    name=i
    p = name.replace("-"," ")
    print(p)
    sr = 'src="{{ '
    src = sr + f'asset("assets/img/our_team/{name}") '+ '}}"'
    div = f"""
    <div class="col-xl-3 col-lg-4 col-sm-6 mt-4 mt-md-5">
        <div class="slider__item">
            <div class="profile-div">
                <img class="profile-pic" {src} alt="">
            </div>
            <div class="profile-name">
                <h6 class="mb-3">{p.split(".jpg")[0]}</h6>
                <p class="mb-0">HOD-photography</p>
            </div>
            <div class="profile-content text-center">
                <h6 class="">{p.split(".jpg")[0]}</h6>
                <p class="fs-16">HOD-photography</p>
                <p class="fs-13 profile-more">
                    ipsum dolor
                    sit amet, consectetur adipisicing elit. Magni, natus sed soluta necessitatibus tempore
                    aspernatur?
                    Praesentium, Magni, natus sed soluta
                    odit explicabo distinctio dolore adipisci officia iure, ut magnam optio aliquam at
                    similique Magni, natus sed soluta
                    veritatis.
                </p>
            </div>
        </div>
    </div>
    """
    file.write(div)
    file.write("\n")
    # time.sleep(60)
    