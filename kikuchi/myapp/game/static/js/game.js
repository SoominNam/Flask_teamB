CANVAS_WIDTH = window.innerWidth * 0.4
CANVAS_HEIGHT = window.innerHeight * 0.8

class Game{
    constructor(){
        // canvasの準備
        this.canvas = document.createElement("canvas");
        document.getElementById("game").appendChild(this.canvas);
        this.canvas.id = "canvas";
        this.canvas.width = CANVAS_WIDTH; 
        this.canvas.height = CANVAS_HEIGHT;
        this.context = this.canvas.getContext("2d");

        this.context.beginPath();
        this.context.fillStyle = "#000000";
        this.context.fillRect(0,0,CANVAS_WIDTH, CANVAS_HEIGHT);
        
        // スタートボタン
        this.context.strokeStyle = "#00FFFF";
        this.context.beginPath();
        this.context.arc(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, CANVAS_HEIGHT/2, 0, Math.PI * 2)
        this.context.fill();
        this.context.stroke();

        let text = "スペースでスタート";
        this.context.font = "50px serif";
        this.context.fillStyle  = "#00FFFF";
        let textVolume = this.context.measureText( text );
        let textWidth = textVolume.width;
        let textHeight = textVolume.actualBoundingBoxAscent;
        this.context.beginPath();
        this.context.fillText( text, (CANVAS_WIDTH-textWidth)/2, (CANVAS_HEIGHT+textHeight)/2);
        this.context.stroke();
    }

    start(){
        this.timeStart = Date.now();
        this.timestop = false;
        this.ans = (Math.random() * 7 + 3)*1000;
        this.flag = true;
        
        //console.log(this.ans)
        this.context.beginPath();
        this.context.fillStyle = "#000000";
        this.context.fillRect(0,0,CANVAS_WIDTH, CANVAS_HEIGHT);

        let text = "赤い丸が表示されたらスペース";
        this.context.font = "30px serif";
        this.context.fillStyle  = "#00FFFF";
        let textVolume = this.context.measureText( text );
        let textWidth = textVolume.width;
        let textHeight = textVolume.actualBoundingBoxAscent;
        this.context.beginPath();
        this.context.fillText( text, (CANVAS_WIDTH-textWidth)/2, (CANVAS_HEIGHT+textHeight)/2);
        this.context.stroke();

        setTimeout(()=>{
            if (this.flag){
                this.context.fillStyle  = "#FF0000";
                this.context.strokeStyle = "#FF0000";
                this.context.beginPath();
                this.context.arc(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, CANVAS_HEIGHT/2, 0, Math.PI * 2);
                this.context.fill();
                this.context.stroke();
            }
        },this.ans)
    }

    stop(){
        let resulttext = "";
        
        let result = false;
        if(this.timestop){
            result = Math.round(this.timestop - (this.timeStart + this.ans));
            resulttext = `記録：${result}ms`;
        }
        else{
            resulttext = `失格`;
            result = false;
        }
        this.context.beginPath();
        this.context.fillStyle = "#000000";
        this.context.fillRect(0,0,CANVAS_WIDTH, CANVAS_HEIGHT);

        this.context.font = "30px serif";
        this.context.fillStyle  = "#00FFFF";
        let resulttextVolume = this.context.measureText( resulttext );
        let resulttextWidth = resulttextVolume.width;
        let resulttextHeight = resulttextVolume.actualBoundingBoxAscent;
        this.context.beginPath();
        this.context.fillText( resulttext, (CANVAS_WIDTH-resulttextWidth)/2, (CANVAS_HEIGHT+resulttextHeight)/2);
        this.context.stroke();
        return result;
    }
}

const playGame = () => {
    var game = new Game();
    var playing = false;
    document.addEventListener('keyup', (event)=>{
        //console.log(event.code);
        if (event.code == "Space" && !playing){
            playing = true;
            game.start();
        }
    });
    document.addEventListener('keypress', (event)=>{
        if (event.code == "Space" && game.flag){
            if(Date.now() - game.timeStart >= game.ans){
                game.timestop = Date.now();
            }else{
                game.timestop = false;
            }
            game.flag = false;
            let result = game.stop();
            if(result){
                let input_socre = document.getElementById("InputScore");
                input_socre.value = result;
                //console.log(result);
                document.getElementById("pushScore").style.display = "block";
                let v = document.getElementById("InputScore").value;
                document.getElementById("resultText").textContent = `${v} みり秒`;
            }
            else{
                document.getElementById("retry").style.display = "block";
            }
        }
    });
}


