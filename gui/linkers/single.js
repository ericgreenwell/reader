function read_single() {
  
  var python = require("python-shell")
  var path = require("path")

  var options = {
    scriptPath : path.join(_dirname, '/../engine/')
    //pythonPath : '/usr/local/bin/python'
  }

  var single = new python('single.py', options);

  single.on('message', function(message) {
    swal("SUCCESS");
  }
}
