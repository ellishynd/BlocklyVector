/* TODO: Change toolbox XML ID if necessary. Can export toolbox XML from Workspace Factory. */
var toolbox = document.getElementById("toolbox");

var options = { 
	toolbox : toolbox, 
	collapse : true, 
	comments : true, 
	disable : true, 
	maxBlocks : Infinity, 
	trashcan : true, 
	horizontalLayout : false, 
	toolboxPosition : 'start', 
	css : true, 
	media : './scripts/media/', 
	rtl : false, 
	scrollbars	 : true, 
	sounds : true, 
	oneBasedIndex : true
};

/* Inject your workspace */ 
var workspace = Blockly.inject("blockly-div", options);

var url = "http://127.0.0.1:8000"

$('#runButton').click(function() {

  var code = Blockly.Python.workspaceToCode(workspace);

  console.log('Running...')
  
  $.post( url, code, function() {
	  console.log('Done!')
  });
})