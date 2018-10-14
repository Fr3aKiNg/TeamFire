from flask import Flask, request, jsonify
import check
app = Flask(__name__)
app.debug = True


@app.route("/", methods=['GET', 'POST'])
def run():
	# global data
	data = request.form['fname']
	# data1 = request.form['fname1']
	# print(data)
	check.readFile("a")
	# check.usercheck("https://www.preventionweb.net/risk/climate-change")
	# check.user_define('1', data)
	return jsonify({'value': check.usercheck(data)})
	# return check.usercheck(data)
