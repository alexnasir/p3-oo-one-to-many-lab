class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # Return the list of pets that belong to the owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        # Check if the pet is an instance of Pet and add the owner to the pet
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        pet.owner = self

    def get_sorted_pets(self):
        # Return the list of pets sorted by their names
        pets_owned_by_me = self.pets()
        return sorted(pets_owned_by_me, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Validate pet_type against PET_TYPES
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Valid types are: {', '.join(Pet.PET_TYPES)}.")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        # Add this instance to the all list
        Pet.all.append(self)
        
        # If an owner is provided, associate it with the pet
        if isinstance(owner, Owner):
            owner.add_pet(self)
        elif owner is not None:
            raise Exception("Owner must be an instance of the Owner class.")