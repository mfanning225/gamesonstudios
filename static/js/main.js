





// SNAKE GAME


// const canvas = document.getElementById('game');
// const ctx = canvas.getContext('2d');

// class SnakePart{
//     constructor(x, y){
//         this.x = x;
//         this.y = y;
//     }
// }

// canvas.width = 529;
// canvas.height = 529;

// let speed = 7;

// let tileCount = 23;
// let tileSize = canvas.width / tileCount - 2;

// let headX = 10;
// let headY = 10;

// const snakeParts = [];
// let tailLength = 2;

// let appleX = 5;
// let appleY = 5

// let xVelocity=0;
// let yVelocity=0;

// let score = 0;


// // game loop
// function drawGame() {
//     changeSnakePosition();

//     let result = isGameOver();
//     if(result){
//         return;
//     }

//     clearScreen();
//     checkAppleCollision();
//     drawApple();
//     drawSnake();
//     drawScore();

//     // Increase speed/difficulty
//     if(score > 2){
//         speed = 6;
//     }
//     if (score > 5){
//         speed = 10;
//     }
//     if (score > 10){
//         speed = 14;
//     }
//     if (score > 15){
//         speed = 18;
//     }


//     setTimeout(drawGame, 1000/ speed);
// }

// function isGameOver(){
//     let gameOver = false;

//     if(yVelocity === 0 && xVelocity === 0) {
//         return false;
//     }

//     //walls
//     if(headX  < 0) {
//         gameOver = true;
//         document.getElementById('highScore').value = score;

       
//     }
//     if(headX === tileCount) {
//         gameOver = true;
//         document.getElementById('highScore').value = score;


//     }
//     else if (headX === tileCount) {
//         gameOver = true;
//         document.getElementById('highScore').value = score;


//     }
//     else if (headY < 0) {
//         gameOver = true;
//         document.getElementById('highScore').value = score;


//     }
//     else if (headY === tileCount) {
//         gameOver = true;
//         document.getElementById('highScore').value = score;


//     }

//     for (let i =0; i < snakeParts.length; i++) {
//         let part = snakeParts[i];
//         if(part.x == headX && part.y === headY) {
//             gameOver = true;
//             document.getElementById('highScore').value = score;
//             break;
//         }
//     }

//     if (gameOver) {
//         ctx.fillStyle = "white";
//         ctx.font = "50px Verdana";

//         ctx.fillText("Game Over!", canvas.width / 6.5, canvas.height / 2)
//         document.getElementById("submit").click();
      
//     }

//     return gameOver;
// }

// function drawScore() {
//     ctx.fillStyle = "white";
//     ctx.font = "10px Verdana";
//     ctx.fillText("Score " + score, canvas.width-50, 10)
// }

// function clearScreen() {
//     ctx.fillStyle = 'black';
//     ctx.fillRect(0,0,canvas.clientWidth,canvas.height);
// }


// function drawSnake() {

//     ctx.fillStyle = 'green';
//     for (let i = 0; i < snakeParts.length; i++) {
//         let part = snakeParts[i];
//         ctx.fillRect(part.x * tileCount, part.y * tileCount, tileSize, tileSize)
//     }

//     snakeParts.push(new SnakePart(headX, headY)); 
//     if(snakeParts.length > tailLength){
//         snakeParts.shift();
//     }

//     ctx.fillStyle = 'orange';
//     ctx.fillRect(headX * tileCount, headY * tileCount, tileSize,tileSize)
// }

// function changeSnakePosition() {
//     headX = headX + xVelocity;
//     headY = headY + yVelocity;
// }

// function drawApple() {
//     ctx.fillStyle = "red";
//     ctx.fillRect(appleX * tileCount, appleY * tileCount, tileSize,tileSize)
// }

// function checkAppleCollision() {
//     if (appleX === headX && appleY == headY) {
//         appleX = Math.floor(Math.random() * tileCount);
//         appleY = Math.floor(Math.random() * tileCount);
//         tailLength++;
//         score++;
//     }
// }

// document.body.addEventListener('keydown', keyDown);

// function keyDown(event) {
//     //up keycode
//     if (event.keyCode == 38) {
//         if(yVelocity == 1)
//             return;
//         yVelocity = -1;
//         xVelocity = 0;
//     }
//     // down
//     if (event.keyCode == 40) {
//         if(yVelocity == -1)
//             return;
//         yVelocity = 1;
//         xVelocity = 0;
//     }
//     //left
//     if (event.keyCode == 37) {
//         if(xVelocity == 1)
//             return;
//         yVelocity = 0;
//         xVelocity = -1;
//     }
//     // right
//     if (event.keyCode == 39) {
//         if(xVelocity == -1)
//             return;
//         yVelocity = 0;
//         xVelocity = 1;
//     }
// }




// drawGame();

window.addEventListener("keydown", function(e) {
    if(["Space","ArrowUp","ArrowDown","ArrowLeft","ArrowRight"].indexOf(e.code) > -1) {
        e.preventDefault();
    }
}, false);



// Testing snake
var canvas = document.getElementById('game');
// var canvas = document.querySelector('canvas');
// var ah = 500
// var aw = 400
// canvas.width = window.innerWidth - aw ;
// canvas.height = window.innerHeight - ah;
canvas.width = 529;
canvas.height = 529;
var display = document.getElementsByTagName('h3');
var ctx  = canvas.getContext('2d');
var grid = 16;
var count = 0;
var score = 0;
var level = 100;
var levelC = 0;
var attempt = 0;
var highScore = 0;
var snake = {
  x: 160,
  y: 160,
  dx: grid,
  dy: 0,
  cells: [],
  maxCells: 4
};
var apple = {
  x: 320,
  y: 320
};






function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}
function startGame() {


  requestAnimationFrame(startGame);
  if (++count < level ) {
    return;
  }

  count = 0;
  ctx.clearRect(0,0,canvas.width,canvas.height);
  snake.x += snake.dx;
  snake.y += snake.dy;
  
  snake.cells.unshift({x: snake.x, y: snake.y});
  if (snake.cells.length > snake.maxCells) {
    snake.cells.pop();
    
  }

  ctx.fillStyle = '#21A179';
  ctx.fillRect(apple.x, apple.y, grid-1, grid-1);

  ctx.fillStyle = '#FB9F89';
 
  snake.cells.forEach(function(cell, index) {
    

    ctx.fillRect(cell.x, cell.y, grid-1, grid-1);  
    
    if (cell.x === apple.x && cell.y === apple.y) {
      snake.maxCells++;
        score = score +5;
        document.getElementById('highScore').value = score;
         level =  level - 1;
          levelC++;
        apple.x = getRandomInt(0, (canvas.width / 25)) *grid;
       apple.y = getRandomInt(0, (canvas.height/ 25)) * grid;

      display[0].innerHTML=("Score:"+score);
      display[3].innerHTML=("Level:"+levelC);
       
    }
  
    for (var i = index + 1; i < snake.cells.length; i++) {
      
      if (snake.x < 0 || snake.x >= canvas.width || snake.y < 0 ||snake.y >= canvas.height  || cell.x === snake.cells[i].x && cell.y === snake.cells[i].y) {
          document.getElementById("submit").click();
          reset();
        init();
      }
  
    }
 
  });

}

// function isGameOver(){
//   let gameOver = false;

//   for (var i = index + 1; i < snake.cells.length; i++) {
//     gameOver = true;
//     document.getElementById("submit").click();


    
//     if (snake.x < 0 || snake.x >= canvas.width || snake.y < 0 ||snake.y >= canvas.height  || cell.x === snake.cells[i].x && cell.y === snake.cells[i].y) {
//       gameOver = true;
//       document.getElementById("submit").click();
//       //init();
//     }

//   }
//   return gameOver;

// }

document.addEventListener('keydown', function(e) {
//left and a  
  if (e.which === 37 || e.which === 65) {
     if(snake.dx === 0){
    snake.dx = -grid;
    snake.dy = 0;
    }
  }
  //up and w 
  else if (e.which === 38 || e.which === 87) {
    if(snake.dy === 0){
    snake.dy = -grid;
    snake.dx = 0;
  }}
  //right and d
  else if (e.which === 39 || e.which === 68 ) {
    if(snake.dx === 0){
    snake.dx = grid;
    snake.dy = 0;
  }
  }
  // down and s
  else if (e.which === 40 || e.which === 83 && snake.dy === 0) {
    if(snake.dy === 0){
    snake.dy = grid;
    snake.dx = 0;
  }}
});
function reset (){
  
         //  console.log("in reset")
        snake.x = 160;
        snake.y = 160;
        snake.cells = [];
        snake.maxCells = 4;
        snake.dx = grid;
        snake.dy = 0;
        apple.x = getRandomInt(0, 25) * grid ;
        apple.y = getRandomInt(0, 25) * grid  ;
        //console.log("Game Over")
        if(score >= highScore || highScore == ''){
        highScore = score}
        attempt++
        //console.log(highScore)
        score = 0;
        level = 5;
        levelC = 0;
  display[0].innerHTML=("Score:"+ score);
  display[3].innerHTML=("Level:"+ levelC);
  display[1].innerHTML=("highScore:"+ highScore);
  display[2].innerHTML=("attempt:"+ attempt);
        //console.log("Calling reset")
}
function init(){
//console.log("in init")
let temp = ctx.getImageData(0,0,canvas.width,canvas.height)   
canvas.width = window.innerWidth - aw;
canvas.height = window.innerHeight  - ah;
 ctx.putImageData(temp,0,0) 

}


// Touch Test
let pageWidth = window.innerWidth || document.body.clientWidth;
let treshold = Math.max(1,Math.floor(0.01 * (pageWidth)));
let touchstartX = 0;
let touchstartY = 0;
let touchendX = 0;
let touchendY = 0;

const limit = Math.tan(45 * 1.5 / 180 * Math.PI);
//const gestureZone = document.getElementById('modalContent');

canvas.addEventListener('touchstart', function(event) {
    event.preventDefault()  
  touchstartX = event.changedTouches[0].screenX;
    touchstartY = event.changedTouches[0].screenY;
}, false);

canvas.addEventListener('touchend', function(event) {
      event.preventDefault()
    touchendX = event.changedTouches[0].screenX;
    touchendY = event.changedTouches[0].screenY;
    handleGesture(event);
}, false);

function handleGesture(e) {
    let x = touchendX - touchstartX;
    let y = touchendY - touchstartY;
    let xy = Math.abs(x / y);
    let yx = Math.abs(y / x);
    if (Math.abs(x) > treshold || Math.abs(y) > treshold || snake.dx === 0 ) {
        if (yx <= limit) {
            if (x < 0) {
                console.log("left");
              if (snake.dx === 0){ 
              snake.dx = -grid;
               snake.dy = 0;};
            } else {
                console.log("right");
              if (snake.dx === 0){
              snake.dx = grid;
               snake.dy = 0;}
            }
        }
        if (xy <= limit) {
            if (y < 0 ) {
                console.log("top");
              if (snake.dy === 0){
              
              snake.dy = -grid;
                    snake.dx = 0;}
            } else {
           
              console.log("bottom");
              if (snake.dy === 0){
                 snake.dy = grid;
                snake.dx = 0;
            }}
        }
    } else {
        console.log("tap");
    }
}
//



//Instruction
function check(){
  //if(window.innerHeight > window.innerWidth){
   //   alert("Please use Landscape! Mode");
  //}
   // else {
    
    init()
    
  
    //init()
  //}
  }
  
  document.addEventListener('DOMContentLoaded', function() {
    alert("Controls \n (MAC/PC) \n  W,S,D,A,UP, DOWN, LEFT,RIGHT \n  (iOS/Android) \n Swipe UP, Swipe Down, Swipe Left, Swipe Right");
    
  check();
  requestAnimationFrame(startGame);
  
  
  }, false);
  
  
  //if (window.DeviceOrientationEvent) {
  //    window.addEventListener('orientationchange', function() { check(); }, false);
  //}
  
  window.onresize = function (event) {
    check();
  }
  //requestAnimationFrame(startGame)
  requestAnimationFrame(startGame);


// Login page javascript

