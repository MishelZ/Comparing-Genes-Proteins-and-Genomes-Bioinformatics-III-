
EnemyDestructor.prototype.update = function () {	
	//chase after destructor
	if (this.isDead != true && destructor.isDead == false){
	//we want to make sure that the destructor is moving towards the players destructor
		    if(destructor.drawX  < (this.drawX ) ) {this.dirx = -this.speed;} 
		    if(destructor.drawX  > (this.drawX) ){this.dirx = this.speed; }
		    if(destructor.drawY < this.drawY){this.diry = -this.speed; }
		    if(destructor.drawY > this.drawY){this.diry = this.speed; }
	}	
	// if palyers destroyer is dead, chase after the players buildersbuilders
	else if (this.isDead != true && numberOfBuilders > 0 && Constructor_player_array[0].isDead == false){
		if(Constructor_player_array[0].drawX  < (this.drawX ) ) {this.dirx = -this.speed;} 
		    if(Constructor_player_array[0].drawX  > (this.drawX) ){this.dirx = this.speed; }
			if(Constructor_player_array[0].drawY < this.drawY){this.diry = -this.speed; }
			if(Constructor_player_array[0].drawY > this.drawY){this.diry = this.speed; }
			
		}		
		else if (this.isDead != true && numberOfBuilders > 1 && Constructor_player_array[1].isDead == false){
			if(Constructor_player_array[1].drawX  < (this.drawX ) ) {this.dirx = -this.speed;} 
		    if(Constructor_player_array[1].drawX  > (this.drawX) ){this.dirx = this.speed; }
			if(Constructor_player_array[1].drawY < this.drawY){this.diry = -this.speed; }
			if(Constructor_player_array[1].drawY > this.drawY){this.diry = this.speed; }			
		}
			else if (this.isDead != true && numberOfBuilders > 2 && Constructor_player_array[2].isDead == false){
			if(Constructor_player_array[2].drawX  < (this.drawX ) ) {this.dirx = -this.speed;} 
		    if(Constructor_player_array[2].drawX  > (this.drawX) ){this.dirx = this.speed; }
			if(Constructor_player_array[2].drawY < this.drawY){this.diry = -this.speed; }
			if(Constructor_player_array[2].drawY > this.drawY){this.diry = this.speed; }			
		}
			else if (this.isDead != true && numberOfBuilders > 3 && Constructor_player_array[3].isDead == false){
			if(Constructor_player_array[3].drawX  < (this.drawX ) ) {this.dirx = -this.speed;} 
		    if(Constructor_player_array[3].drawX  > (this.drawX) ){this.dirx = this.speed; }
			if(Constructor_player_array[3].drawY < this.drawY){this.diry = -this.speed; }
			if(Constructor_player_array[3].drawY > this.drawY){this.diry = this.speed; }			
		}
		else if (this.isDead != true && numberOfBuilders > 4 && Constructor_player_array[4].isDead == false){
			if(Constructor_player_array[4].drawX  < (this.drawX ) ) {this.dirx = -this.speed;} 
		    if(Constructor_player_array[4].drawX  > (this.drawX) ){this.dirx = this.speed; }
			if(Constructor_player_array[4].drawY < this.drawY){this.diry = -this.speed; }
			if(Constructor_player_array[4].drawY > this.drawY){this.diry = this.speed; }			
		}
		//if players destroyer and all builders are dead, chasing after the building
		//I send the AI destructor to the top of the building, it not perfect, but most of the bricks will be destroyed
		else if (this.isDead != true && numberOfBricks_for_destruction > 0){
			if(Bricks_player_array[numberOfBricks_for_destruction-1].drawX  < (this.drawX ) ) {this.dirx = -this.speed;} 
		    if(Bricks_player_array[numberOfBricks_for_destruction-1].drawX  > (this.drawX) ){this.dirx = this.speed; }
			if(Bricks_player_array[numberOfBricks_for_destruction-1].drawY < this.drawY){this.diry = -this.speed; }
			if(Bricks_player_array[numberOfBricks_for_destruction-1].drawY > this.drawY){this.diry = this.speed; }
		}
		//if players destroyer, builders and miners are dead, AI will be chashing miners
		else if (this.isDead != true && numberOfMiners > 0 && Miners_player_array[0].isDead == false){
			if(Miners_player_array[0].drawX  < (this.drawX ) ) {this.dirx = -this.speed;} 
		    if(Miners_player_array[0].drawX  > (this.drawX) ){this.dirx = this.speed; }
			if(Miners_player_array[0].drawY < this.drawY){this.diry = -this.speed; }
			if(Miners_player_array[0].drawY > this.drawY){this.diry = this.speed; }
		}
		
		else if (this.isDead != true && numberOfMiners > 1 && Miners_player_array[1].isDead == false){
			if(Miners_player_array[1].drawX  < (this.drawX ) ) {this.dirx = -this.speed;} 
		    if(Miners_player_array[1].drawX  > (this.drawX) ){this.dirx = this.speed; }
			if(Miners_player_array[1].drawY < this.drawY){this.diry = -this.speed; }
			if(Miners_player_array[1].drawY > this.drawY){this.diry = this.speed; }
		}
		else if (this.isDead != true && numberOfMiners > 2 && Miners_player_array[2].isDead == false){
			if(Miners_player_array[2].drawX  < (this.drawX ) ) {this.dirx = -this.speed;} 
		    if(Miners_player_array[2].drawX  > (this.drawX) ){this.dirx = this.speed; }
			if(Miners_player_array[2].drawY < this.drawY){this.diry = -this.speed; }
			if(Miners_player_array[2].drawY > this.drawY){this.diry = this.speed; }
			
		}
		else if (this.isDead != true && numberOfMiners > 3 && Miners_player_array[3].isDead == false){
			if(Miners_player_array[3].drawX  < (this.drawX ) ) {this.dirx = -this.speed;} 
		    if(Miners_player_array[3].drawX  > (this.drawX) ){this.dirx = this.speed; }
			if(Miners_player_array[3].drawY < this.drawY){this.diry = -this.speed; }
			if(Miners_player_array[3].drawY > this.drawY){this.diry = this.speed; }
			
		}
		else if (this.isDead != true && numberOfMiners > 4 && Miners_player_array[4].isDead == false){
			if(Miners_player_array[4].drawX  < (this.drawX ) ) {this.dirx = -this.speed;} 
		    if(Miners_player_array[4].drawX  > (this.drawX) ){this.dirx = this.speed; }
			if(Miners_player_array[4].drawY < this.drawY){this.diry = -this.speed; }
			if(Miners_player_array[4].drawY > this.drawY){this.diry = this.speed; }
		}
		//if pleyer does not have any destroers, builders, building or miners, AI destroyer will not move	
		else{
			this.dirx =0;
			this.diry = 0;
		}
		//update the draw coordinates for the AI destroyer
		this.drawX = this.drawX + this.dirx;
		this.drawY =  this.drawY + this.diry;
		//prevent runof screen, if new this.drawX and this.drawY are not on canvas, place the AI destroyer back to canvas
		//600 is the max height of canvas
		if(this.drawY >= (600 -this.height)){
			this.drawY = (600 -this.height);
		}
		if(this.drawY<0){
			this.drawY = 0;
		}
		//800 is the max width of canvas
		if(this.drawX >= (800 -this.width)){
			this.drawX = (800 -this.width);
		}
		if(this.drawX <0){
			this.drawX = 0;
		}
		//finally draw the AI destroyer on canvas	
		ctxEntities.drawImage(imgSprite,this.xpos5,this.ypos5,this.width, this.height,this.drawX, this.drawY,this.width, this.height);
			
   
};

function checkHittingEnemyDestructor () {
	    if (collision(enemydestructor, destructor) && enemydestructor.isDead == false && destructor.isDead == false && !destructor.isHitting && destructor.isSpacebar == false) {
			if(innerMeterPlayer.width > 0){
				innerMeterPlayer.width = (innerMeterPlayer.width - 50);
			} 
			if(innerMeterPlayer.width == 0){
				destructor.die();
				numberOfDestructors = 0;
				//clearInterval(enemydestractor.moveInterval);
				document.getElementById("destructor").innerHTML = numberOfDestructors;
			} 
	           
        }
		
	 for (var i = 0; i < Miners_player_array.length; i++) {
        if (collision(Miners_player_array[i], enemydestructor)&& enemydestructor.isDead == false && Miners_player_array[i].isDead == false){
			Miners_player_array[i].die();
			numberOfMiners2 = numberOfMiners2 - 1;
			document.getElementById("miner").innerHTML = numberOfMiners2;
			
		}
	 }
		
	 for (var i = 0; i < Constructor_player_array.length; i++) {
        if (collision(Constructor_player_array[i], enemydestructor)&& enemydestructor.isDead == false && Constructor_player_array[i].isDead == false){
			Constructor_player_array[i].die();
			numberOfBuilders2 = numberOfBuilders2 - 1;
			document.getElementById("builder").innerHTML = numberOfBuilders2;
			
		}
	 }
	 
	 
	 		//destroying players bricks		
	for (var i = 0; i < Bricks_player_array.length; i++) {
   		if (collision(enemydestructor, Bricks_player_array[i]) && Bricks_player_array[i].isDead == false && enemydestructor.isDead == false) {
			numberOfBricks_for_destruction = numberOfBricks_for_destruction-1;
			Bricks_player_array[i].die();
			document.getElementById("player_height").innerHTML = numberOfBricks_for_destruction;
			
		} 
	}
};

//collision detection, for more information refer to the following resource
//https://retrosnob.files.wordpress.com/2014/10/foundation-game-design-with-html5-and-javascript-v413hav-1.pdf
function collision(a, b) {	
	var vx = (a.drawX+ (a.width/2)) - (b.drawX+ (b.width/2));
	var vy = (a.drawY+ (a.height/2)) - (b.drawY+ (b.height/2));
	var magnitude = Math.sqrt(vx*vx +vy*vy);
	var totalRadii = a.width/2 + b.width/2;
	var hit = magnitude < totalRadii;
	return hit;
}