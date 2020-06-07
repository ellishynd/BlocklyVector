Blockly.defineBlocksWithJsonArray([{
  "type": "vector_pickup_cube",
  "message0": "pickup cube",
  "previousStatement": null,
  "nextStatement": null,
  "colour": 120,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "vector_play_animation",
  "message0": "play animation %1",
  "args0": [
    {
      "type": "field_dropdown",
      "name": "play_animation",
      "options": [
        [
          "greeting",
          "ReactToGreeting"
        ],
        [
          "good morning",
          "ReactToGoodMorning"
        ],
        [
          "good night",
          "ReactToGoodNight"
        ],
        [
          "bye bye",
          "ReactToGoodBye"
        ]
      ]
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 120,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "vector_speak_text",
  "message0": "say text %1",
  "args0": [
    {
      "type": "input_value",
      "name": "speak_text",
      "check": "String"
    }
  ],
  "inputsInline": true,
  "previousStatement": null,
  "nextStatement": null,
  "colour": 120,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "vector_lift_range",
  "message0": "lift range %1",
  "args0": [
    {
      "type": "field_number",
      "name": "lift_range",
      "value": 1,
      "min": 1,
      "max": 100
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 120,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "vector_head_range",
  "message0": "head range %1",
  "args0": [
    {
      "type": "field_number",
      "name": "head_range",
      "value": 30,
      "min": 1,
      "max": 100
    }
  ],
  "previousStatement": null,
  "nextStatement": null,
  "colour": 120,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "vector_wheels_turn",
  "message0": "turn %1",
  "args0": [
    {
      "type": "input_value",
      "name": "wheels_turn",
      "check": "Number"
    }
  ],
  "inputsInline": true,
  "previousStatement": null,
  "nextStatement": null,
  "colour": 120,
  "tooltip": "",
  "helpUrl": ""
},
{
  "type": "vector_wheels_drive",
  "message0": "drive",
  "message1": "distance %1 speed %2",
  "args1": [
    {
      "type": "input_value",
      "name": "distance",
      "check": "Number"
    },
    {
      "type": "field_number",
      "name": "speed",
      "value": 20,
      "min": 1,
      "max": 100
    }
  ],
  "inputsInline": true,
  "previousStatement": null,
  "nextStatement": null,
  "colour": 120,
  "tooltip": "",
  "helpUrl": ""
}])