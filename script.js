const title = document.getElementById("title");
const hint = document.getElementsByClassName("hint")[0]
var start = false;
var i = 0;
let text = [
    "ого","текст изменился", "снова!", "почему?","на текст нажали","...",
    "может сделать текст цветным?","оранжевый?","похож на интересный сайт",
    "красный?","интересный цвет","он похож на кровь.", "...", "зелёный?", 
    "он такой яркий", "трава тоже зелёная", "синий?", "цвет неба", 
    "пустого неба", "оно пустое?", "я не знаю.", "а какой цвет ночи?", 
    "ночь", "она тёмная", "почему здесь частичка тёмного среди белого?", 
    "может так будет лучше?", "белая частичка посреди тёмного...", 
    "а чего тёмного?", "это пространство", "это тёмный цвет - цвет ночи", 
    "мы видим ночь через небо?", "на небе есть звёзды ночью?", "есть", 
    "фиолетовый?", "он как вечер", "что происходит вечером?", "я не знаю", 
    "а днём?", "я не знаю", "что обычно происходит?", "сон", "почему?", "не знаю",
    "просто мечтаю", "я хочу спать", "почему?", "мне плохо", "всё постоянно повторяется",
    "это тоже повторится?", "..."
];

function changeText(){
    if (!start){hint.style.display = "none";start=true;}
    

    title.textContent = text[i];
    console.log(i);
    
    
    if (i == 6) title.style.color = "#FFA500";
    if (i == 8) title.style.color = "#FF0000";
    if (i == 12) title.style.color = "#00FF00";
    if (i == 15) title.style.color = "#87CEEB";
    if (i == 21){ title.style.color = "black"; document.body.style.backgroundColor = "white"; };
    if (i == 24){ title.style.color = "white"; document.body.style.backgroundColor = "black"; };
    if (i == 32){ title.style.color = "#8A2BE2" };
    if (i == 35){ title.style.color = "white" };
    if (i == 49){ i=-1}

    i++;
}