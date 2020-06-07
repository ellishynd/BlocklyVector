Blockly.Python['vector_pickup_cube'] = function(block) {
  var code = 'vector.pickup_cube()\n';
  return code;
};

Blockly.Python['vector_play_animation'] = function(block) {
  var dropdown_play_animation = block.getFieldValue('play_animation');
  var code = `vector.play_animation("${dropdown_play_animation}")\n`;
  return code;
};

Blockly.Python['vector_speak_text'] = function(block) {
  var value_speak_text = Blockly.Python.valueToCode(block, 'speak_text', Blockly.Python.ORDER_ATOMIC);
  var code = `vector.speak_text(${value_speak_text})\n`;
  return code;
};

Blockly.Python['vector_lift_range'] = function(block) {
  var number_lift_range = block.getFieldValue('lift_range');
  var code = `vector.lift_height(${number_lift_range})\n`;
  return code;
};

Blockly.Python['vector_head_range'] = function(block) {
  var number_head_range = block.getFieldValue('head_range');
  var code = `vector.head_angle(${number_head_range})\n`;
  return code;
};

Blockly.Python['vector_wheels_turn'] = function(block) {
  var value_wheels_turn = Blockly.Python.valueToCode(block, 'wheels_turn', Blockly.Python.ORDER_ATOMIC);
  var code = `vector.wheels_turn(${value_wheels_turn})\n`;
  return code;
};

Blockly.Python['vector_wheels_drive'] = function(block) {
  var value_distance = Blockly.Python.valueToCode(block, 'distance', Blockly.Python.ORDER_ATOMIC);
  var number_speed = block.getFieldValue('speed');
  var code = `vector.wheels_drive(${value_distance}, ${number_speed})\n`;
  return code;
};