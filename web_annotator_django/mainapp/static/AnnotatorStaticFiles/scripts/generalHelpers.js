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
  ctx.font = '20px serif';
  ctx.strokeStyle = 'green';
  ctx.lineWidth = 0.5;
  ctx.fillStyle = 'yellow';
  ctx.fillText(text, x, y);
  ctx.strokeText(text, x, y);
}

function resetDraw(canvasid){
  var ctx = document.getElementById(canvasid).getContext('2d');
  ctx.clearRect(0, 0, 10000, 10000); // 10,000 is a big enough num of pixels to clear :)
}

function changeElementInnerHTML(elementId, newInnerHTML){
	element = document.getElementById(elementId);
	element.innerHTML = newInnerHTML;
}

function removeAnnotationFromArray( annos_array, annotation ) {
	index = annos_array.findIndex((cur_anno) => (cur_anno.text == annotation.text && cur_anno.shapes == annotation.shapes))
	annos_array.splice(index,1); // remove the item from the array
}
function addAnnotationToArray( annos_array, annotation ) {
	annos_array.push(annotation);
}
function editAnnotationInArray( annos_array, annotation ) {
	index = annos_array.findIndex((cur_anno) => cur_anno.shapes == annotation.shapes)
	annos_array[index].text = annotation.text;
}
// transforms the position from precents to pixels and returns the bottom-left corner
function getTextPostition(annotation) {
	x = annotation.shapes[0].geometry.x*img_element.width;
	y = (annotation.shapes[0].geometry.y + annotation.shapes[0].geometry.height*0.7)*img_element.height;
	return {left: x, top: y};
}