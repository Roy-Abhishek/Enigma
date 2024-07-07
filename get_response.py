from Functionality.enigma import Enigma
import Functionality.constants as constants

def get_response(user_message):
    return "this is the test response you get"

def encode(input, plugboard_dict, rotor1_info, rotor2_info, rotor3_info, rotor1_index, rotor2_index, rotor3_index, reflector_list):
    enigma = Enigma()

    enigma.change_plugboard(constants.PLUGBOARD_CONFIGS[plugboard_dict])
    enigma.change_rotors(constants.ROTOR_INFOS[rotor1_info],
                         constants.ROTOR_INFOS[rotor2_info],
                         constants.ROTOR_INFOS[rotor3_info])
    enigma.set_rotor_index_settings(int(rotor1_index), int(rotor2_index), int(rotor3_index))
    if reflector_list != "default":
        enigma.change_reflector_settings(constants.OTHER_OPTIONAL_REFLECTOR_RANDOMIZE_LISTS[reflector_list])

    encoded_code = enigma.encode(input, enigma.rotor1_starting_index, enigma.rotor2_starting_index, enigma.rotor3_starting_index)

    return encoded_code
    

def decode(input, plugboard_dict, rotor1_info, rotor2_info, rotor3_info, rotor1_index, rotor2_index, rotor3_index, reflector_list):
    enigma = Enigma()

    enigma.change_plugboard(constants.PLUGBOARD_CONFIGS[plugboard_dict])
    enigma.change_rotors(constants.ROTOR_INFOS[rotor1_info],
                         constants.ROTOR_INFOS[rotor2_info],
                         constants.ROTOR_INFOS[rotor3_info])
    enigma.set_rotor_index_settings(int(rotor1_index), int(rotor2_index), int(rotor3_index))
    if reflector_list != "default":
        enigma.change_reflector_settings(constants.OTHER_OPTIONAL_REFLECTOR_RANDOMIZE_LISTS[reflector_list])

    encoded_code = enigma.decode(input, enigma.rotor1_starting_index, enigma.rotor2_starting_index, enigma.rotor3_starting_index)

    return encoded_code

