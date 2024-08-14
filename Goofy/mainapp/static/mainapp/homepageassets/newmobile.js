

function lnav() {
    document.getElementById("goofy-ham").classList.toggle("hidden");
    document.getElementById("leftnav").classList.toggle("hidden");
    const navelements = ["home", "explore", "library", "likedsongs","profile"];
    for (const i of navelements) {

        document.getElementById(i).classList.toggle("sm:hidden");

    }
    if (expanded) {
        if (window.innerWidth >= 768) {
            document.getElementById("allelements").classList.remove("md:ml-[280px]");
            if (document.getElementById("allelements1")) {
                
                document.getElementById("allelements1").classList.remove("md:ml-[280px]");
            }
            document.getElementById("searchbox").classList.remove("md:ml-[280px]");
        }
        else
        {

            document.getElementById("allelements").classList.remove("blur-sm");
            if (document.getElementById("allelements1")) {
                
                document.getElementById("allelements1").classList.add("blur:sm");
            }
            document.getElementById("searchbox").classList.remove("blur-sm");
            document.getElementById("searchbox").classList.remove("sm:ml-[240px]");
            document.getElementById("logo").classList.remove("blur-sm");
            document.getElementById("searchbtn").classList.remove("blur-sm");
        }
        document.getElementById("leftnav").classList.replace("w-[50%]", "w-[17%]");
        document.getElementById("leftnav").classList.replace("w-[240px]", "sm:w-[72px]");
        document.getElementById("leftnav").classList.remove("bg-[#0e0e0a]");
        // document.getElementById("parentscrolldiv").classList.replace("w-[1040px]", "w-[1216px]");
        document.getElementById("hel").classList.replace("*:w-[90%]", "*:w-[80%]");
        document.getElementById("hel").classList.replace("*:pl-2", "*:pl-[14px]");
        document.getElementById("hel").classList.replace("*:ml-3", "*:ml-2");
        document.getElementById("hrnav").classList.replace("mx-5","mx-1.5");
        document.getElementById("profilebox").classList.replace("w-[90%]", "w-[80%]");
        // document.getElementById("profilebox").classList.replace("pl-2", "pl-[10px]");
        // document.getElementById("profilebox").classList.replace("ml-3", "ml-2");
       

       
        expanded = false;
    }
    else {
        if (window.innerWidth >= 768) {
            document.getElementById("allelements").classList.add("md:ml-[280px]");
            if (document.getElementById("allelements1")) {
                
                document.getElementById("allelements1").classList.add("md:ml-[280px]");
            }
            document.getElementById("searchbox").classList.add("md:ml-[280px]");
        }
        else
        {

            document.getElementById("allelements").classList.add("blur-sm");
            if (document.getElementById("allelements1")) {
                
                document.getElementById("allelements1").classList.add("blur:sm");
            }
            document.getElementById("searchbox").classList.add("blur-sm");
            document.getElementById("searchbox").classList.add("sm:ml-[240px]");
            document.getElementById("logo").classList.add("blur-sm");
            document.getElementById("searchbtn").classList.add("blur-sm");
        }

        document.getElementById("leftnav").classList.replace("w-[17%]", "w-[50%]");
        document.getElementById("leftnav").classList.replace("sm:w-[72px]", "w-[240px]");
        document.getElementById("leftnav").classList.add("bg-[#0e0e0a]");
        document.getElementById("hel").classList.replace("*:w-[80%]", "*:w-[90%]");
        document.getElementById("hel").classList.replace("*:pl-[14px]", "*:pl-2");
        document.getElementById("hel").classList.replace("*:ml-2", "*:ml-3");
        document.getElementById("hrnav").classList.replace("mx-1","mx-5");
        document.getElementById("profilebox").classList.replace("w-[80%]", "w-[90%]");
        // document.getElementById("profilebox").classList.replace("pl-[10px]", "pl-2");
        // document.getElementById("profilebox").classList.replace("ml-2", "ml-3");

        
        expanded = true;
    }
}


function crossappear() {
    if (document.getElementById("searchcontent").value != "") {
        document.getElementById("searchbox").classList.remove("rounded-2xl");
        document.getElementById("searchbox").classList.add("rounded-t-2xl");
        document.getElementById("searchbox").classList.add("rounded-b-xl");
        document.getElementById("clearcross").classList.remove("hidden");
        document.getElementById("searchbox").classList.replace("bg-[#68686638]", "bg-gray-800");
        document.getElementById("searchsuggestions").classList.remove("hidden");
       


    } else {
        document.getElementById("searchbox").classList.add("rounded-2xl");
        document.getElementById("searchbox").classList.remove("rounded-t-2xl");
        document.getElementById("searchbox").classList.remove("rounded-b-xl");
        document.getElementById("clearcross").classList.add("hidden");

        document.getElementById("searchbox").classList.replace("bg-gray-800", "bg-[#68686638]");

        document.getElementById("searchsuggestions").classList.add("hidden");
 
        closesearch();
    }
    // setTimeout(search(document.getElementById("searchcontent").value, 7),500);
    
}

function clearinput() {
    document.getElementById("searchcontent").value = "";
    crossappear();
}

function searchboxappear()
{
    document.getElementById("logo").classList.add("hidden");
    document.getElementById("ham").classList.add("hidden");
    document.getElementById("searchbtn").classList.add("hidden");
    document.getElementById("searchbox").classList.remove("hidden");
    document.getElementById("searchbox").classList.replace("w-[70%]","w-[90%]");
    document.getElementById("searchbox").classList.add("ml-2.5");
    document.getElementById("searchcontent").focus();

    
}


function closesearch() {
    document.getElementById("logo").classList.remove("hidden");
    // document.getElementById("ham").classList.remove("hidden");
    document.getElementById("searchbtn").classList.remove("hidden");
    document.getElementById("searchbox").classList.add("hidden");
    document.getElementById("searchbox").classList.replace("w-[90%]","w-[70%]");
    document.getElementById("searchbox").classList.remove("ml-2.5");
    document.getElementById("searchsuggestions").classList.add("hidden");
           
}


function horizontalscroll(left,eleid) {
    if (left) {
        document.getElementById(eleid).scrollLeft -= 200;
    } else {
        document.getElementById(eleid).scrollLeft += 200;
    }

}


function clickmanage(event) {
    // Close the search content
    if (!document.getElementById("searchcontent").contains(event.target) && 
        !document.getElementById("searchbtn").contains(event.target) &&  
        !document.getElementById("searchpic").contains(event.target)) {
        closesearch();
    }

    // Close the left navigation
    if (!document.getElementById("leftnav").classList.contains("hidden") && 
        !document.getElementById("leftnav").contains(event.target) && 
        !document.getElementById("ham2").contains(event.target)) {
        lnav();
    }

    // Close the playlist dropdown
    document.querySelectorAll('.playlist-dropdown').forEach(dropdown => {
        const button = dropdown.previousElementSibling;
        if (dropdown.contains(event.target) || !button.contains(event.target)) {
            dropdown.classList.add('hidden');
        }
    });
}


document.getElementById("searchcontent").addEventListener("input", crossappear);
document.body.addEventListener("click",clickmanage);

document.getElementById("explorebox").addEventListener("mouseenter", () => {
    document.getElementById("exploreimg").classList.add("animate-spin");
});
document.getElementById("explorebox").addEventListener("mouseleave", () => {
    document.getElementById("exploreimg").classList.remove("animate-spin");
});