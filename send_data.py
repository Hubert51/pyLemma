from flask import Flask
from flask import request
from flask import render_template

import main
import sys

# sys.setrecursionlimit(10000)

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my_form.html")

@app.route('/', methods=['POST'])
def my_form_post():

    # text = request.form['text0']
    sectionNum = 0
    sectionName = 'text'+str(sectionNum)+'[]' 
    file = open('Examples/test.txt', 'w')
    texts = request.form.getlist('rules[]')

    for rule in texts:
        file.write(rule)
        file.write('\n')
    file.write('\n')


    texts = request.form.getlist(sectionName)
    # print len(texts) 
    while(texts!=[]):
        file.write('proof\n')
        index_copy = 0
    	for index in range(len(texts)-1):
            # this is first line of sub proof
            # print index
            if index!=0 and (index==1 or index_copy%4==1 ):
                file.write('\n')
            file.write(texts[index])
            if index_copy%4==0 or texts[index+1]=='' or texts[index+1]=='done':
                index_copy += 1
                continue
            file.write('\t')
            index_copy += 1

        file.write('\n\n')


        sectionNum += 1
        sectionName = 'text'+str(sectionNum)+'[]' 
    	texts = request.form.getlist(sectionName)
    # 	print texts

    # for text in texts:
    # 	print text
    file.close()
    output = main.pyLemma('test.txt')
    # print text[0]

    # print text[1]
    # print text[2]
    # print text[3]
    # print request.form['text2'][2]
    # output = output.split('\n')
    print output
    return render_template('show_result.html',items=output)#,items = answer)

if __name__ == '__main__':
    app.run(debug=True)