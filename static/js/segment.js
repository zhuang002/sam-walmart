
class Segment {
    constructor(sec) {
        this.root = document.createElement('div');
        this.root.className = "segment";
        var title = document.createElement('div');
        title.className = "segment_title";
        title.innerText = sec.name;
        this.root.appendChild(title);
        var categories = document.createElement('div');
        categories.className = "segment_categories";
        this.root.appendChild(categories);
        for (var i=0;i<sec.categories.length;i++) {
            var tp = new TextPicture(sec.categories[i]);
            categories.appendChild(tp.getRoot());
        }
    }

    getRoot() {
        return this.root;
    }
}