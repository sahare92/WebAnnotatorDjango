function gray(imgObj) {
	var canvas = document.createElement('canvas');
	var canvasContext = canvas.getContext('2d');
	
	var imgW = imgObj.width;
	var imgH = imgObj.height;
	canvas.width = imgW;
	canvas.height = imgH;
	
	canvasContext.drawImage(imgObj, 0, 0);
	var imgPixels = canvasContext.getImageData(0, 0, imgW, imgH);
	
	for(var y = 0; y < imgPixels.height; y++){
		for(var x = 0; x < imgPixels.width; x++){
			var i = (y * 4) * imgPixels.width + x * 4;
			var avg = (imgPixels.data[i] + imgPixels.data[i + 1] + imgPixels.data[i + 2]) / 3;
			imgPixels.data[i] = avg; 
			imgPixels.data[i + 1] = avg; 
			imgPixels.data[i + 2] = avg;
		}
	}
	canvasContext.putImageData(imgPixels, 0, 0, 0, 0, imgPixels.width, imgPixels.height);
	return canvas.toDataURL();
}

function draw(canvasid, text, x, y) {
  var ctx = document.getElementById(canvasid).getContext('2d');
  ctx.font = '24px serif';
  ctx.strokeStyle = 'red';
	  ctx.lineWidth = 0.5;
  ctx.fillStyle = 'black';
  ctx.fillText(text, x, y);
  ctx.strokeText(text, x, y);
}

function changeElementInnerHTML(elementId, newInnerHTML){
	element = document.getElementById(elementId);
	element.innerHTML = newInnerHTML;
}