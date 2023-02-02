<p>[[部署]]
[[服务器]]
[[阿里云]]</p>
<h1 id="intr">Intr</h1>
<p><strong>FTP</strong>:  Flie Transfer Protocol</p>
<p><strong>Benefit:</strong>
-  Faster than HTTP
-  Built in Mac</p>
<h1 id="todo-在阿里云上部署">TODO 在阿里云上部署</h1>
<h1 id="q-为什么在macos等类linux-上的sshftp如此build-in而win需要第三方软件ssh它们只是一种协议吗">Q : 为什么在macOS等类linux 上的ssh,ftp如此build-in，而Win需要第三方软件，SSH它们只是一种协议吗？</h1>
<h1 id="在云服务器上部署ftp">在云服务器上部署FTP</h1>
<p>[[FTP]]</p>
<p><a href="https://help.aliyun.com/document_detail/60152.html?spm=5176.10173289.help.dexternal.c5e02e77uGJVja&amp;scm=20140722.S_help%40%40文档%40%4060152.S_hot%2Bos0.ID_60152-RL_FTP-LOC_consoleUNDhelp-OR_ser-V_2-P0_0">官方教程</a></p>
<h2 id="整体逻辑">整体逻辑</h2>
<ol>
<li>开启ftp服务</li>
<li>在服务器创建一个 用于 <code>ftp</code> 的user，并给它准备一个own是它的文件夹(方便管理读写权限)</li>
<li>在配置文件中使用本地用户模式 #Q 那这种ftp的认证是否类似于远程登录</li>
<li>修改一系列的配置文件</li>
</ol>
<h2 id="软件与配置文件">软件与配置文件</h2>
<h3 id="服务相关">服务相关</h3>
<ul>
<li>
<p>设置FTP服务开机自启动 <code>systemctl enable vsftpd.service</code></p>
</li>
<li>
<p>启动FTP服务 <code>systemctl start vsftpd.service</code></p>
</li>
<li>
<p>查看FTP服务端口号 <code>netstat -antup | grep ftp</code></p>
</li>
<li>
<p>关闭防火墙 <code>systemctl stop firewalld</code></p>
</li>
</ul>
<h3 id="配置文件">配置文件</h3>
<ul>
<li>vsftp.conf 在 <code>etc/vsftpd.conf</code></li>
</ul>
<h4 id="权限配置">权限配置</h4>
<ul>
<li>在<code>vim /etc/vsftpd/chroot_list</code>中加入的用户可以访问其他目录</li>
</ul>
<h4 id="配置文件参数说明">配置文件参数说明</h4>
<p>/etc/vsftpd目录下文件说明如下：</p>
<ul>
<li>/etc/vsftpd/vsftpd.conf是vsftpd的核心配置文件。</li>
<li>/etc/vsftpd/ftpusers是黑名单文件，此文件中的用户不允许访问FTP服务器。</li>
<li>/etc/vsftpd/user_list是白名单文件，此文件中的用户允许访问FTP服务器。</li>
</ul>
<p>配置文件vsftpd.conf参数说明如下：</p>
<table>
<thead>
<tr>
<th>参数</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>anonymous_enable=YES</td>
<td>接受匿名用户</td>
</tr>
<tr>
<td>no_anon_password=YES</td>
<td>匿名用户login时不询问口令</td>
</tr>
<tr>
<td>anon_root=（none)</td>
<td>匿名用户主目录</td>
</tr>
<tr>
<td>local_enable=YES</td>
<td>接受本地用户</td>
</tr>
<tr>
<td>local_root=（none）</td>
<td>本地用户主目录</td>
</tr>
<tr>
<td>用户权限控制参数说明如下表所示</td>
<td></td>
</tr>
</tbody>
</table>
<table>
<thead>
<tr>
<th>参数</th>
<th>说明</th>
</tr>
</thead>
<tbody>
<tr>
<td>write_enable=YES</td>
<td>可以上传文件（全局控制）</td>
</tr>
<tr>
<td>local_umask=022</td>
<td>本地用户上传的文件权限</td>
</tr>
<tr>
<td>file_open_mode=0666</td>
<td>上传文件的权限配合umask使用</td>
</tr>
<tr>
<td>anon_upload_enable=NO</td>
<td>匿名用户可以上传文件</td>
</tr>
<tr>
<td>anon_mkdir_write_enable=NO</td>
<td>匿名用户可以建目录</td>
</tr>
<tr>
<td>anon_other_write_enable=NO</td>
<td>匿名用户修改删除</td>
</tr>
<tr>
<td>chown_username=lightwiter</td>
<td>匿名上传文件所属用户名</td>
</tr>
</tbody>
</table>
<h2 id="在阿里云网站上配置防火墙">在阿里云网站上配置防火墙</h2>
<p><img alt="" src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202211250054258.png" /></p>
<h1 id="how-to-use-ftp-on-macos">How to use FTP on macOS</h1>
<h2 id="ui">UI</h2>
<p>在<em>访答</em> 中：</p>
<p><img alt="" src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202211220152277.png" /></p>
<p><img alt="" src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202211220153878.png" /></p>
<h2 id="terminal">Terminal</h2>
<p><code>ftp:// ip-address</code></p>
<p><strong>Commands</strong></p>
<ul>
<li><code>get</code>: will download a single file. Type “get” followed by the name of the file you want to download from the server</li>
<li><code>put</code>: will upload a single file. Type “put” followed by the name of the file you want to upload to the server.</li>
<li><code>quit</code>: will quit your connection to the FTP server.</li>
</ul>
<h2 id="third-party-filezila">Third-party: FileZila</h2>
<ol>
<li>打开FileZilla客户端。</li>
<li>在顶部菜单栏，选择文件 &gt; 站点管理器。</li>
<li>在站点管理器对话框的左下角，单击新站点。</li>
<li>
<p>输入新站点的名称，并完成站点配置。
        <img alt="" src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202211250104974.png" /></p>
<p>具体的配置项说明如下：</p>
<ul>
<li>新站点名称：您自定义的站点名称。例如<code>test-01</code>。</li>
<li>协议：FTP-文件传输协议。</li>
<li>主机：FTP服务器公网IP地址。本文中为Linux实例的公网IP地址，例如<code>121.43.XX.XX</code>。</li>
<li>端口：21。</li>
<li>登录类型：匿名。</li>
</ul>
</li>
<li>
<p>单击连接。
    <img alt="" src="https://mypicsformarkdown.oss-cn-shanghai.aliyuncs.com/imgs/202211250105041.png" /></p>
</li>
</ol>
<p>连接成功后，您可以对文件进行上传、下载和删除等操作。FileZilla工具界面如下图所示</p>
<p>①显示命令、FTP连接状态和任务执行结果。</p>
<p>②本地区域，显示本地主机的目录信息。</p>
<p>③远程区域，显示FTP服务器的目录信息。匿名模式下，默认目录为/pub。</p>
<p>④记录区域，可查看FTP任务的队列信息和日志信息。</p>
<h1 id="secure">Secure</h1>
<p>FTP was not designed to be secure.</p>
<ul>
<li>clear-text</li>
<li>lack of encryption</li>
</ul>
<p>can use TLS, SFTP, SSL for secure</p>