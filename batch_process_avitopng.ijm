input = "/Users/isabellawang/Documents/BME548/Project/Hikoavis/";
list = getFileList(input);
for (i=0; i<list.length; i++) {
	filename = list[i];
	open(input+filename);
	selectWindow(filename);
	run("Image Sequence... ", "dir=/Users/isabellawang/Documents/BME548/Project/Hikopngs/ format=PNG");
}
