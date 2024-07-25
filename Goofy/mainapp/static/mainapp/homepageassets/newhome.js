

function heading1material() {


    const songscroll = document.getElementById("parentscrolldiv1");

    if (!songscroll) {
        console.error("Element with ID 'parentscrolldiv1' not found");
        return;
    }

    const elementstr = `
        <div>
            <div class="h-40 w-40 border-white border-2">
                <img src="${staticUrl}" alt="">
            </div>
            <div class="text-white w-40 pt-1">
                Song Name
            </div>
            <div class="text-white w-40">
                Artist Name
            </div>
        </div>`;

    for (let i = 0; i < 10; i++) {
        const parser = new DOMParser();
        const newelements = parser.parseFromString(elementstr, "text/html").body.firstChild;
        songscroll.appendChild(newelements);
    }
}

function createribbon() {
    const genres = {"Relax":"bg-gradient-to-r from-[#467b3d] via-[#b0f1a5] to-[#467b3d]", "Energize":"bg-gradient-to-r from-[#b4843b] via-[#f7e0bc] to-[#b4843b]", "Romance":"bg-gradient-to-r from-[#7a2828] via-[#d29393] to-[#7a2828]", "Sad":"bg-gradient-to-r from-[#8951FF] via-[#C8AEFF] to-[#8951FF]", "Sleep":"bg-gradient-to-r from-[#66DDEE] via-[#B3F5FF] to-[#66DDEE]", "Podcasts":"bg-gradient-to-r from-[#FF75C5] via-[#FFB6E0] to-[#FF75C5]"};
    const ribbox = document.getElementById("ribbonbox");
    const parser = new DOMParser();
    Object.entries(genres).forEach(([ele,k]) => {
        ribbox.appendChild(parser.parseFromString(`<div>
        <button class="${k} mr-2 text-black text-lg font-semibold border-white border-[3px] rounded-lg hover:shadow-lg hover:shadow-white hover:scale-110">
            <div class="px-5 py-1 text-xl">${ele}</div>
        </button>
    </div>`, "text/html").body.firstChild);
    });
}



function heading5material() {
    const songscroll = document.getElementById("parentscrolldiv4");
    const elementstr = `<div>
    <div class="h-40 w-40 border-white border-2">
        <img src="{% static 'mainapp/homepageassets/songdp.svg' %}" alt="">
    </div>
    <div class="text-white w-40 pt-1">
        Song Name
    </div>
    <div class="text-white w-40">
        Artist Name
    </div>
</div>`
    const parser = new DOMParser();
    const newelements = parser.parseFromString(elementstr, "text/html").body.firstChild;
    for (let i = 0; i < 10; i++) {
        songscroll.appendChild(newelements.cloneNode(true));
    }
}
function heading4material() {
    const songscroll = document.getElementById("h4");
    const elementstr = `<div>
    <div class="flex space-x-2">
                            <div class="border-white border-2"><img src="{% static 'users/songsmalldp.svg' %}"
                                    ></div>
                            <div>
                                <div>Song Name</div>
                                <div>Artists Name</div>
                            </div>
                        </div>
</div>`
    const parser = new DOMParser();
    const newelements = parser.parseFromString(elementstr, "text/html").body.firstChild;
    for (let i = 0; i < 9; i++) {
        songscroll.appendChild(newelements.cloneNode(true));
    }
}

function horizontalscroll(left,eleid) {
    if (left) {
        document.getElementById(eleid).scrollLeft -= 200;
    } else {
        document.getElementById(eleid).scrollLeft += 200;
    }

}


function handleresize()
{
    const ribbonbox = document.getElementById('ribbonbox');
    if (window.innerWidth>=911) {
        ribbonbox.classList.remove('overflow-x-scroll');
        document.getElementById('parentscrolldiv1').classList.remove('overflow-x-auto');
        document.getElementById('parentscrolldiv2').classList.remove('overflow-x-auto');
        document.getElementById('parentscrolldiv3').classList.remove('overflow-x-auto');
        document.getElementById('parentscrolldiv5').classList.remove('overflow-x-auto');
        // document.getElementById('h4').classList.remove('overflow-x-auto');
    }
    if (window.innerWidth<911) {
        ribbonbox.classList.add('overflow-x-scroll');
        document.getElementById('parentscrolldiv1').classList.add('overflow-x-auto');
        document.getElementById('parentscrolldiv2').classList.add('overflow-x-auto');
        document.getElementById('parentscrolldiv3').classList.add('overflow-x-auto');
        document.getElementById('parentscrolldiv5').classList.add('overflow-x-auto');
        // document.getElementById('h4').classList.add('overflow-x-auto');
    }
    if (window.innerWidth == 768 && !expanded)
        {
            lnav();
        }
    else if(window.innerWidth < 768 && expanded)
        {
            lnav();
        }    
}


// handleresize();
// window.addEventListener("resize",handleresize);

// heading1material();
createribbon();
// heading1material();
// heading2material();
// heading3material();
// heading4material();
// heading5material();

