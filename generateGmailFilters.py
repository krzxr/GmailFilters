from pandas import isna, read_csv, DataFrame

def setEntry(filter_rule:list):
    entry = ''

    ENTRY_TEMPLATE_HEAD = r'''
    	<entry>
    		<category term='filter'></category>
    		<title>Mail Filter</title>
    		<content></content>'''+"\n"
    ENTRY_TEMPLATE_TAIL = r'</entry>'+"\n"

    for property, value in filter_rule:
        entry+='\t\t\t'+r"<apps:property name='" +property+ r"' value='" + value +r"'/>"+"\n"
    entry+='\t\t\t'+r"""<apps:property name='sizeOperator' value='s_sl'/>"""+"\n\t\t\t"+\
		"""<apps:property name='sizeUnit' value='s_smb'/>"""+"\n"
    return ENTRY_TEMPLATE_HEAD+entry+'\t\t'+ENTRY_TEMPLATE_TAIL


FILE_TEMPLATE_HEAD = r'''<?xml version='1.0' encoding='UTF-8'?>
<feed xmlns='http://www.w3.org/2005/Atom' xmlns:apps='http://schemas.google.com/apps/2006'>
	<title>Mail Filters</title>
	'''
FILE_TEMPLATE_TAIL = r'</feed>'

IS_OR = 'OR?'
LABEL = 'label'

CSV_INPUT = 'emailFiltersInput.csv'
input = read_csv(CSV_INPUT)
df = DataFrame(input)
numRow = len(df.index)
colList = list(df.columns)
colList.remove(IS_OR)
colList.remove(LABEL)

xmlContent = ''

for row_idx in range(numRow):
    label = df[LABEL].iat[row_idx]
    isOrRule = df[IS_OR].iat[row_idx]
    # OR Rule: buz meaning: properties are linked via OR
    # -> tech implicaiton: call setEntry for each property
    if isOrRule:

        for column_name in colList:
            entry = df[column_name].iat[row_idx]
            if not isna(entry):
                rule = [(LABEL,label),(column_name,entry)]
                xmlEntry = setEntry(rule)
                xmlContent+=xmlEntry
    else:
        rules = [(LABEL,label)]
        for column_name in colList:
            entry = df[column_name].iat[row_idx]
            if not isna(entry):
                rules.append((column_name,entry))
        xmlEntry = setEntry(rules)
        xmlContent+=xmlEntry

fileContent = FILE_TEMPLATE_HEAD + xmlContent + FILE_TEMPLATE_TAIL

file = open('emailFilters.xml','w',encoding='utf8')
file.write(fileContent)
file.close()


