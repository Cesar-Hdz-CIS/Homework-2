#Cesar Hernandez 1835494
init_pass = input()
#print(init_pass)
a_edit = init_pass.replace('a','@')
i_edit = a_edit.replace('i','!')
m_edit = i_edit.replace('m','M')
B_edit = m_edit.replace('B', '8')
o_edit = B_edit.replace('o', '.')
final_pass = o_edit + 'q*s'
print(final_pass)