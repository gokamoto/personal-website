# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    # return "Hello, World!"  # return a string
    return render_template('index.html')  # render a template

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

	# 	<script>
	# 	  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
	# 	  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
	# 	  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
	# 	  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

	# 	  ga('create', 'UA-63571509-1', 'auto');
	# 	  ga('send', 'pageview');

	# 	</script>