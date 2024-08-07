function createribbon() {
    // const genres = {"New Releases":"bg-gradient-to-r from-[#7a2828] via-[#d29393] to-[#7a2828]", "Trending":"bg-gradient-to-r from-[#FF75C5] via-[#FFB6E0] to-[#FF75C5]", "Mood & Genres":"bg-gradient-to-r from-[#467b3d] via-[#b0f1a5] to-[#467b3d]", "Top Artists":"bg-gradient-to-r from-[#66DDEE] via-[#B3F5FF] to-[#66DDEE]"};
    const genres = ["New Releases","Top Playlists","Mood & Genres","Trending Albums"];

    const ribbox = document.getElementById("ribbonbox");
    const parser = new DOMParser();
    genres.forEach(ele => {
        ribbox.appendChild(parser.parseFromString(`<div>
        <a class=" mr-2 text-white hover:text-black text-lg   hover:bg-[#1d88e6] rounded-full hover:border-white border-2 border-[#1d88e6]  hover:shadow-white hover:scale-110 " href="#">
            <div class="px-5 py-1 text-xl">${ele}</div>
        </a>
    </div>`, "text/html").body.firstChild);
});
}



function heading1material() {
    const songscroll = document.getElementById("parentscrolldiv1");
    const elementstr = `<div>
    <div class="h-40 w-40 border-white border-2">
        <img src="newassets/songdp.svg" alt="">
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
function heading2material() {
    const songscroll = document.getElementById("parentscrolldiv2");
    const elementstr = `<div>
    <div class="h-40 w-40 border-white border-2">
        <img src="newassets/songdp.svg" alt="">
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


function moodandgenres() {
    const moods = {
        "1": "bg-[#8FFF7D]",
        "2":"bg-[#FFC061]",
        "3": "bg-[#FF5A5A]",
        "4": "bg-[#A57BFF]",
        "5": "bg-[#76DEFF]",
        "6": "bg-[#FF75C5]",
        "7": "bg-[#FF75C5]",
        "8": "bg-[#8FFF7D]",
        "9": "bg-[#FFC061]",
        "10": "bg-[#FF5A5A]",
        "11": "bg-[#A57BFF]",
        "12": "bg-[#76DEFF]",
        "13": "bg-[#76DEFF]",
        "14": "bg-[#FF75C5]",
        "15": "bg-[#8FFF7D]",
        "16": "bg-[#FFC061]",
        "17": "bg-[#FF5A5A]",
        "18": "bg-[#A57BFF]",
        "19": "bg-[#A57BFF]",
        "20": "bg-[#76DEFF]",
        "21": "bg-[#FF75C5]",
        "22": "bg-[#8FFF7D]",
        "23": "bg-[#FFC061]",
        "24": "bg-[#FF5A5A]",
        "25": "bg-[#FF5A5A]",
        "26": "bg-[#A57BFF]",
        "27": "bg-[#76DEFF]",
        "28": "bg-[#FF75C5]",
        "29": "bg-[#8FFF7D]",
        "30": "bg-[#FFC061]",
        "31": "bg-[#FFC061]",
        "32": "bg-[#FF5A5A]",
        "33": "bg-[#A57BFF]",
        "34": "bg-[#76DEFF]",
        "35": "bg-[#FF75C5]",
        "36": "bg-[#8FFF7D]"
    };
    const mandg = document.getElementById("mandg");
    const parser = new DOMParser();
    Object.entries(moods).forEach(([ele,k]) =>{
        mandg.appendChild(parser.parseFromString(`<div>
        <button class="${k} mr-2 text-black text-lg font-semibold border-white border-[3px] rounded-lg hover:shadow-lg hover:shadow-white hover:scale-110 justify-stretch min-w-full">
            <div class="px-5 py-1 text-xl">${ele}</div>
        </button>
    </div>`,"text/html").body.firstChild);
    });
}



function heading4material() {
    const songscroll = document.getElementById("parentscrolldiv4");
    const elementstr = `<div>
    <div class="h-40 w-40 border-white border-2">
        <img src="newassets/artistdp.svg" alt="">
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






// createribbon();
// heading1material();
// heading2material();
// heading4material();
// moodandgenres();