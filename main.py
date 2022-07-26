from owlready2 import *
from openpyxl import Workbook


def render_using_name(entity):
     return entity.name


set_render_func(render_using_name)

onto = get_ontology("Silvanus ontology(con seeAlso).owl").load()

wb = Workbook()
ws = wb.active

classes = list(onto.classes())
# with open("classes.csv", "w", encoding="UTF8") as f:
line = 2
for c in classes:
    if c.comment:
        desc = c.comment[0].replace("\n", " ")
    else:
        desc = ""
    sources = list()
    if c.source:
        for s in c.source:
            sources.append(s)
    if c.seeAlso:
        for s in c.seeAlso:
            sources.append(s)
    # line = f"{c}§{desc}§{c.is_a}§{list(c.subclasses())}§{sources}\n"
    # f.write(line)
    parents = map(str, list(c.is_a))
    subclasses = map(str, list(c.subclasses()))
    print(list(subclasses))

    ws[f"A{line}"] = "Class name"
    ws[f"A{line+1}"] = "Class description"
    ws[f"A{line+2}"] = "Class parents"
    ws[f"A{line+3}"] = "Subclasses"
    ws[f"A{line+4}"] = "Sources"

    ws[f"B{line}"] = str(c)
    ws[f"B{line+1}"] = desc
    ws[f"B{line+2}"] = ", ".join(parents)
    ws[f"B{line+3}"] = ", ".join(subclasses)
    ws[f"B{line+4}"] = ", ".join(sources)
    line += 6

wb.save("onto.xlsx")