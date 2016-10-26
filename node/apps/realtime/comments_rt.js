var commentController = function(io,querystring,http){

      io.sockets.on('connection', function(socket){

        //CREATE COMMENTS
      	socket.on('new comment', function(data){
      		var values = querystring.stringify(data);
      		var options = {
      			hostname: 'localhost',
      			port: '8000',
      			path: '/comments/newcomment',
      			method: 'POST',
      			headers: {
      				'Content-Type': 'application/x-www-form-urlencoded',
      				'Content-Length': values.length
      			}
      		};
      		var req = http.request(options, function(res){
      			res.setEncoding('utf8');
      			res.on('data', function(data){
      				io.sockets.emit('show comment', data);
      			});
      		});
      		req.write(values);
      		req.end();
      	});
      });
};

module.exports = commentController;
