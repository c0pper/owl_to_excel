from main import onto, render_using_name, classes, properties

# fire_subclasses = onto.Fire.subclasses()
# spatial_subclasses = onto.Spatial_entity.subclasses()

def subclasses_list_to_str(onto_class):
    subclasses = list(onto_class.subclasses())
    if len(subclasses) > 0:
        if len(subclasses) == 2:
            subclass1 = subclasses[0].name.replace("_", " ")
            subclass2 = subclasses[1].name.replace("_", " ")
            subclasses_str = f"{subclass1}\" and \"{subclass2}"
        else:
            subclasses_str = "\", \"".join(list(map(render_using_name, subclasses))).replace("_", " ")
        if onto_class.comment:
            return_str = f"\"{onto_class.name.replace('_', ' ')}\" class contains \"" + subclasses_str + f"\". {onto_class.comment[0]}"
        else:
            return_str = f"\"{onto_class.name.replace('_', ' ')}\" class contains \"" + subclasses_str + f"\"."
        if return_str[-1] != ".":
            return_str += "."
        print(return_str)


def get_prop_desc_for_class(class_):
    for p in properties:
        name = p.name.replace("_", " ")
        domain = list(map(render_using_name, p.domain))
        range = list(map(render_using_name, p.range))
        if class_.name in domain or class_.name in range:
            domani_str = "\", \"".join(domain).replace("_", " ")
            range_str = "\", \"".join(range).replace("_", " ")
            # if p.comment:
            #     ret_str = f'Property "{name}" links class "{domani_str}" to class "{range_str}". {p.comment[0]}'
            # else:
            #     ret_str = f'Property "{name}" links class "{domani_str}" to class "{range_str}"'
            ret_str = f'Property "{name}" links class "{domani_str}" to class "{range_str}"'
            if ret_str[-1] != ".":
                ret_str += "."
            print(ret_str)

def print_subclasses_and_props(class_):
    classes_ = list(class_.subclasses())
    if len(classes_) > 0:
        if len(classes_) == 2:
            subclass1 = classes_[0].name.replace("_", " ")
            subclass2 = classes_[1].name.replace("_", " ")
            subclasses_str = f"{subclass1}\" and \"{subclass2}"
        else:
            subclasses_str = "\", \"".join(list(map(render_using_name, classes_))).replace("_", " ")
    print(f'The main classes in this area are "{subclasses_str}".')
    for c in classes_:
        subclasses_list_to_str(c)
    print("Regarding properties, those that affect this macro-area are the following:")
    get_prop_desc_for_class(class_)


classes_ = list(onto.individuals())
# classes_ = [onto.Biodiversity_index, onto.Vegetated_area, onto.Vegetation_stat, onto.Living_being_stat, onto.Sensor, onto.Climate_parameter, onto.Response_resource, onto.Monitored_area, onto.Vulnerable_object]
for c in classes_:
    print(type(c), c)
    # print_subclasses_and_props(c)
    print("\n\n")

list(default_world.sparql("""
           SELECT (COUNT(?x) AS ?nb)
           { ?x a owl:Class . }
    """))