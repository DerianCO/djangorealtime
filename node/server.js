var io = require('socket.io').listen(8008);
var http = require('http');
var querystring = require('querystring');

require('./apps/realtime/comments_rt')(io,querystring,http);
