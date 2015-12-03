_author__ = 'alex'
import sys
import xml.dom.minidom as dom

def get_Res_Matrix(length,nodes,nets_d,elem_type):
    Res = [[[] for j in range(length)] for i in range(length)]
    for i in range(nodes.length):
        if nodes[i].nodeType != elem_type: continue
        name = nodes[i].nodeName
        if name == "diode":
            net_from, net_to = nets_d[(int)(nodes[i].getAttribute("net_from"))], nets_d[(int)(nodes[i].getAttribute("net_to"))]
            res, rev_res = (float)(nodes[i].getAttribute("resistance")), (float)(nodes[i].getAttribute("reverse_resistance"))
            Res[net_from][net_to].append(res)
            Res[net_to][net_from].append(rev_res)
        else:
            if name == "capactor" or name == "resistor":
                net_from, net_to = nets_d[(int)(nodes[i].getAttribute("net_from"))], nets_d[(int)(nodes[i].getAttribute("net_to"))]
                res = (float)(nodes[i].getAttribute("resistance"))
                Res[net_from][net_to].append(res)
                Res[net_to][net_from].append(res)
    return Res

def parse_xml():
    elem_type = dom.Element.ELEMENT_NODE
    doc = dom.parse(sys.argv[1])
    #parse xml
    for node in doc.childNodes:
        if node.nodeName == "schematics": break
    nodes = node.childNodes
    nets_d = {}
    for i in range(nodes.length):
        if nodes[i].nodeType != elem_type: continue
        if nodes[i].nodeName != "net": continue
        nets_d[(int)(nodes[i].getAttribute("id"))] = 0
    length = 0
    for x in sorted(nets_d):
        nets_d[x] = length
        length += 1
    return nodes,nets_d,elem_type,length
if __name__ == "__main__":
    if len(sys.argv) <> 3:
        print("check the arguments")
        exit()

    nodes,nets_d,elem_type,length = parse_xml()
    Res = get_Res_Matrix(length,nodes,nets_d,elem_type)
    print Res
