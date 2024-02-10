//board 
let tileSize = 32;
let rows = 20;
let columns = 20;

let board;
let boardWidth = tileSize * columns;
let boardHeight = tileSize * rows;
let context;

//ship
let shipWidth = tileSize *2;
let shipHeight = 50;
let shipX = tileSize * columns / 2 - tileSize;
let shipY = tileSize * rows - tileSize * 2;

let ship = {
    x: shipX,
    y: shipY,
    width: shipWidth,
    height: shipHeight
}

let shipImg;
let shipVelocityX = tileSize;

//aliens
let aliens = [];
let alienWidth = tileSize * 2;
let alienHeight = tileSize;
let alienX = tileSize;
let alienY = tileSize;
let alienImg;

let alienRows = 2;
let aliensColumns = 3
let alienCount = 0;
let alienVelocityX = 0.7;

//bullets
let bullets = [];
let bulletImg;
let bulletWidth = tileSize / 2;
let bulletHeight = tileSize / 2;
let bulletVelocityY = -7;

//game over
let score = 0;
let gameOver = false;

window.onload = function(){
    board = document.getElementById("board");
    board.width = boardWidth;
    board.height = boardHeight;
    context = board.getContext("2d");

    shipImg = new Image();
    shipImg.src = "./ship.png";
    shipImg.onload = function(){
        context.drawImage(shipImg, ship.x, ship.y, ship.width, ship.height);
    }

    alienImg = new Image();
    alienImg.src = "./alien-lime.png";
    spawnAliens();

    bulletImg = new Image();
    bulletImg.src = "./bullet.png";
    
    requestAnimationFrame(update);
    document.addEventListener("keydown", moveShip);
    document.addEventListener("keyup", shootBullets);
}

function update(){
    requestAnimationFrame(update);

    if (gameOver){
        return;
    }

    context.clearRect(0, 0, board.width, board.height);

    //ship
    context.drawImage(shipImg, ship.x, ship.y, ship.width, ship.height);

    //alien
    for (let i = 0; i < aliens.length; i++){
        let alien = aliens[i];
        if (alien.alive){
            alien.x += alienVelocityX;

            //alien bounce if touch in borders
            if (alien.x + alien.width >= board.width || alien.x <= 0){
                alienVelocityX *= -1;
                alien.x += alienVelocityX * 2;

                //move down each bounce
                for (let j = 0; j < aliens.length; j++){
                    aliens[j].y += alienHeight;
                }
            }
            context.drawImage(alienImg, alien.x, alien.y, alien.width, alien.height);
            
            //game over conditions
            if (alien.y >= ship.y){
                gameOver = true;
                alert("Game Over!");
            }
        }
    }

    //bullets
    for (let i = 0; i < bullets.length; i++){
        let bullet = bullets[i];
        bullet.y += bulletVelocityY;
        context.drawImage(bulletImg, bullet.x, bullet.y, bullet.width, bullet.height);

        //bullet collision with aliens
        for (let j = 0; j < aliens.length; j++){
            let alien = aliens[j];
            if (!bullet.used && alien.alive && hitAlien(bullet, alien)){
                bullet.used = true;
                alien.alive = false;
                alienCount--;
                score += 100;
            }
        }
    }

    //clear bullets
    while (bullets.length > 0 && (bullets[0].used || bullets[0].y < 0)){
        bullets.shift();
    }

    //next level
    if (alienCount == 0){
        //increase number of aliens
        aliensColumns = Math.min(aliensColumns + 1, columns / 2 - 2);
        alienRows = Math.min(alienRows + 1, rows - 4);
        alienVelocityX += 0.2;
        aliens = [];
        bullets = [];
        spawnAliens();
    }

    //score
    context.fillStyle = "White";
    context.font = "20px courier";
    context.fillText("Score: " + score, 5, 20);
}

function moveShip(e){
    if (gameOver){
        return;
    }

    if (e.code == "ArrowLeft" && ship.x - shipVelocityX >= 0){
        ship.x -= shipVelocityX;
    }
    else if (e.code == "ArrowRight" && ship.x + shipVelocityX + ship.width <= board.width){
        ship.x += shipVelocityX;
    }
}

function spawnAliens(){
    for (let i = 0; i < aliensColumns; i++){
        for (let j = 0; j < alienRows; j++){
            let alien = {
                img: alienImg,
                x: alienX + i * alienWidth,
                y: alienY + j * alienHeight,
                width: alienWidth,
                height: alienHeight,
                alive: true
            }

            aliens.push(alien);
        }
    }
    alienCount = aliens.length;
}

function shootBullets(e){
    if (gameOver){
        return;
    }

    if (e.code == "Space"){
        let bullet = {
            x: ship.x + shipWidth * 15 / 40,
            y: ship.y,
            width: bulletWidth,
            height: bulletHeight,
            used: false
        }
        bullets.push(bullet);
    }
}

function hitAlien(a, b){
    return a.x < b.x + b.width &&   //a's top left corner doesn't reach b's top right corner
           a.x + a.width > b.x &&   //a's top right corner passes b's top left corner
           a.y < b.y + b.height &&  //a's top left corner doesn't reach b's bottom left corner
           a.y + a.height > b.y;    //a's bottom left corner passes b's top left corner
}