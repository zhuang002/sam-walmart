class TextPicture {
    constructor(cat) {
        this.root = document.createElement('a');
        this.root.className = "textPicture";
        var table = document.createElement('table');
        table.style.cellSpacing=0;
        table.style.borderWidth=0;
        this.root.appendChild(table);
        var tr = document.createElement('tr');
        table.appendChild(tr);
        var td = document.createElement('td');
        tr.appendChild(td);

        //var imgDiv = document.createElement("div");
        //imgDiv.class = "textPicture img";
        //this.root.appendChild(imgDiv);
        var img = document.createElement("img");
        img.src = cat.img;
        img.className = "tp_img";
        //imgDiv.appendChild(img);
        //this.root.appendChild(img);
        td.appendChild(img);
        tr = document.createElement('tr');
        table.appendChild(tr);
        td = document.createElement('td');
        tr.appendChild(td);
        var textDiv = document.createElement("div");
        textDiv.className = "tp_text";
        textDiv.innerText = cat.text;
        td.appendChild(textDiv);
        //this.root.appendChild(textDiv);
        this.root.href = cat.link;
    }

    getRoot() {
        return this.root;
    }
}