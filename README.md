<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<!-- 新 Bootstrap 核心 CSS 文件 -->
<link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap.min.css">

<!-- 可选的Bootstrap主题文件（一般不用引入） -->
<link rel="stylesheet" href="http://cdn.bootcss.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">

<!-- jQuery文件。务必在bootstrap.min.js 之前引入 -->
<script src="http://cdn.bootcss.com/jquery/1.11.3/jquery.min.js"></script>

<!-- 最新的 Bootstrap 核心 JavaScript 文件 -->
<script src="http://cdn.bootcss.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
</head>
<body>
<div class="container">
<h1 class="text-center">ipv6Proxy</h1>

<div class="panel panel-default">
  <div class="panel-heading">简介</div>
  <div class="panel-body">
    ipv6Proxy是一款用ipv6做代理的python脚本，主要应用在部分校园，可以通过ipv6来访问获取ipv4上的http网页资源。可以用于跳过ipv4的流量限制。当前属于第一版本，效果不是特别显著，针对某些门户网站的访问效果比较理想。
    同时，当前不支持https协议，故对于墙外的某些著名网站如谷歌、推特也是无力的。
  </div>
</div>

<div class="panel panel-default">
  <div class="panel-heading">原理</div>
  <div class="panel-body">
    在远程服务器上开启ipv6Proxy，将建立一个ipv6socket，然后，将本地的代理指向ipv6socket的ipv6地址，所有的http请求将被转发至ipv6socket上，然后取得http的请求头部，进行相应处理，得到请求方式、请求地址、http协议版本号及其他的头部信息，
    利用所得的头部信息，构造一个新的http请求，通过ipv4socket去向该请求所指向的服务器请求相应的资源，然后将所得的资源通过原有的ipv6socket发送回去。
  </div>
</div>

<div class="panel panel-default">
  <div class="panel-heading">程序目录</div>
  <div class="panel-body">
  目录中含有4个文件：<br/>
  方法:简述原理
  allCommand:用于记录代理过程的文件，可以通过logCommand(String data)来写入
  HTTPRequest.py:用于解析http头部的封装类
  proxy.py:程序主文件，开启代理
  </div>
</div>

<div class="panel panel-default">
  <div class="panel-heading">使用方法</div>
  <div class="panel-body">
  将所有文件上传至远端服务器，改写proxy.py中的HOST为服务器的ip地址(i6地址)<br/>
  使用python proxy.py命令开启代理，也可以置于后台
  在本地将http代理指向服务器，端口为proxy.py中的PORT(可以任意指定，只要不是被限定的端口即可)
  </div>
</div>

<div class="panel panel-default">
  <div class="panel-heading">部分程序解析</div>
  <div class="panel-body">
  <code>
    SocketServer.TCPServer.address_family=socket.AF_INET6<br/>
  server = SocketServer.ThreadingTCPServer(addr,Servers)<br/>
  server.serve_forever()<br/>
  </code>
  这三句用于开启服务线程，每接收到一个代理请求，均开启新的线程进行处理。

  getHttp(data)函数：
  data为收到的请求头部，getHttp函数将处理好头部并代理获取响应http资源。
  </div>
</div>

<div class="panel panel-default">
  <div class="panel-heading">联系方式</div>
  <div class="panel-body">
  
  作者:吴雨培<br/>
  邮箱：840302039@qq.com
  </div>
</div>
</div>
</body>