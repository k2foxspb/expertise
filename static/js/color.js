function MyFunc(cell_name) {
    var Elements = [];
    var SelectedColor = document.getElementById("ColorPicker").value;
    for (var i = 1; i <= 12; i++) {
        Elements[i - 1] = document.getElementById("n" + i.toString()).id;
    }
    for (var i = 0; i < 12; i++) {
        if (cell_name == Elements[i]) continue;
        else document.getElementById(Elements[i]).style.backgroundColor = SelectedColor;
    }
}