input = "/Users/isabellawang/Documents/BME548/Project/BackupAvis/";
directory = getDirectory(input);
list = getFileList(directory);
for (i=0; i<list.length; i++) {
	filename = list[i];
	open(input+filename);
	selectWindow(filename);
	new_folder = "/Users/isabellawang/Documents/BME548/Project/Hikopngs2/"+filename;
	File.makeDirectory(new_folder);
	run("Image Sequence... ", "dir="+new_folder+" format=PNG");
	close();
}
