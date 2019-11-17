from unittest.mock import Mock

# TODO : show in a debug session

# pretending to be a RNA sequence object
rna_sequence = Mock() # a mock object has nothing as it is created

# pretending to have an attribute (or member variable) holding the RNA sequence
rna_sequence.sequence = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"
print(f"sequence: {rna_sequence.sequence}")

# pretending to have a translate() method
rna_sequence.translate.return_value = "MAMAPRTEINSTRING"
print(f"translation: {rna_sequence.translate()}")





# TODO : skip this
# we can specify a function to be used also
import random
rna_sequence.get_random_value.side_effect = random.randint
print(f"random value 1: {rna_sequence.get_random_value(1, 10)}")
print(f"random value 2: {rna_sequence.get_random_value(2, 9)}")
print(f"random value 3: {rna_sequence.get_random_value(3, 8)}")
print(f"random value 4: {rna_sequence.get_random_value(4, 7)}")