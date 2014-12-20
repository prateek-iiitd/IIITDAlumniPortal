<!DOCTYPE html>
<html>
<head>
    <title>Alumni | Give Back</title>
    <link rel="stylesheet" href="http://alumni.iiitd.edu.in/static/bootstrap/css/bootstrap.min.css">
    <link rel="stylesheet" href="http://alumni.iiitd.edu.in/static/alumniportal/css/stylesheet.css">
</head>
<style type="text/css">
input{
	border:1px solid #777777; margin: 10px 0 0;vertical-align: middle;}
</style>
<body>
<!-- Main Element for Full width -->
<div id="nav-bar-main" class="row navbar-fixed-top">
    <div class="container">
        <!-- Element for actual navbar -->
        <div class="row">
            <div class="pull-left">
                <a href="/"><img src="http://alumni.iiitd.edu.in/static/alumniportal/img/alumni-logo.png" style="height:50px;margin-top:15px;"/></a>
            </div>
            <div id="nav-bar" class="pull-right">
                <ul>
                    <a href="http://alumni.iiitd.edu.in/"><li ><span class="nav-bar-font">Home</span></li></a>
                    <a href="http://alumni.iiitd.edu.in/news/"><li ><span class="nav-bar-font">News</span></li></a>
                    <a href="http://alumni.iiitd.edu.in/blog/"><li ><span class="nav-bar-font">Blog</span></li></a>
                    <a href="http://alumni.iiitd.edu.in/directory/"><li ><span class="nav-bar-font">Directory</span></li></a>
                    <a href="http://alumni.iiitd.edu.in/giveback/"><li ><span class="nav-bar-font">Give Back</span></li></a>
                    <a href="http://alumni.iiitd.edu.in/contact_us/"><li ><span class="nav-bar-font">Contact Us</span></li></a>
                </ul>
            </div>
        </div>
    </div>
</div>
<div class="container">
<div class="row">
    <div class="col-lg-offset-1 col-lg-10" id="green-dabba"></div>
</div>
<div id="contentpane" class="row">
<div class="card-main col-lg-9">
     <div class="row no-underline">
        <h2>Donation Pledge Form</h2>
  <FORM name='form' action='donatehdfc.php' method='post' encType= 'multipart/form-data' onSubmit="form.paynow.value='Submitting.. ';form.paynow.disable=true;" >
<table border="0" align="center" cellspacing="5" cellpadding="2" width="100%">
  <TBODY>
  <tr><td colspan="6"><h3>CONTRIBUTOR'S INFORMATION</h3></td></tr>
  <tr>
    <td width="10%">Last Name</td>
    <td width="24%"> <input type="text" name="LName" required /></td>
    <td width="10%" > First Name </td>
    <td width="18%"> <input type="text" name="FName" required /></td>
    <td width="9%" align="center"> MI</td>
    <td width="29%"> <input type="text" name="MI" /></td>
  </tr>
   <tr>
    <td > Address  </td><td colspan="5">    
      <input name="fulladress" type="text" size="89%" required /></td>
    </tr>
    <tr>
    <td> City</td>
    <td> <input type="text" name="city" required /></td> <td > State</td>
    <td> <input type="text" name="state" required  /></td>
    <td align="center"> Pincode</td>
    <td> <input type="text" name="Pincode" max="6" required /></td>
    </tr>

    <tr>
    <td> Telephone</td>
    <td> <input type="tel" name="Mobile" required max="13" placeholder="Digits only" onBlur="check();" /></td>
    <td > Email</td> 
    <td> <input type="email" name="Email" required /></td>
    <td align="center"> PAN </td>
        <td> <input type="text" name="PAN" max="10" required /></td>
  </tr>
      <tr>
      <td> <input type="checkbox" name="anonymous" onClick="form.remark.value += 'Donation as Anonymous'" /></td>
      <td colspan="5">I (we) wish to have my (our) donation remain anonymous.</td>
    </tr>
      <tr>
      <td colspan="6"><br /></td>
      </tr>    
      <tr>
      <td colspan="6"><h3>DONATION INFORMATION</h3></td>
		</tr>
      <tr>
      <td colspan="6"> I pledge to contribute towards: </td></tr>
      <tr> <td> <input type="radio" name="contribiute" value=" Scholarships" checked="checked" onClick="form.remark.value = this.value" /></td><td colspan="5">Scholarships for students for financially weaker sections</td> </tr>
       <tr><td> <input type="radio" name="contribiute" value=" travelgrants" onClick="form.remark.value = this.value"  /></td><td colspan="5">Travel Grants for students for International Conferences</td></tr> 
       <tr><td> <input type="radio" name="contribiute" value=" studentclub" onClick="form.remark.value = this.value"  /></td><td colspan="5">Student Clubs and Activities</td> </tr>
       <tr><td> <input type="radio" name="contribiute" value=" Entrepreneurship" onClick="form.remark.value = this.value"  /></td><td colspan="5">Entrepreneurship Activities</td> </tr>
       <tr><td> <input type="radio" name="contribiute" value=" Teaching" onClick="form.remark.value = this.value"  /></td><td colspan="5">Teaching Excellence Awards</td></tr>
       <tr><td> <input type="radio" name="contribiute" value=" Other" onClick="form.remark.value = this.value"  /></td><td >Others (Please Specify)</td>
       <td colspan="4" align="left"><input type="text" name="OtherOption" onChange="form.remark.value = this.value" /></td></tr>
          </tr>
      <tr>
      <td colspan="6"><br /></td>
      </tr>
<tr><td colspan="2"> <input type="radio" name="doationfrequency" value="one time" checked="checked" onClick="showblock(onetime);hideblock(repeating);twentyfive.checked='checked';form.tamount.value ='25000.00';" /> One-time donation of INR</td>
<td colspan="4"> <input type="radio" name="doationfrequency" value="repeating" onClick="hideblock(onetime);showblock(repeating);form.remark.value+= 'Repeat donation';form.tamount.value ='10000.00';ten.checked='checked';" /> Repeating donation of INR</td></tr>
<tr id="onetime"><td> <input type="radio" name="donation" value="100000.00" onClick="form.tamount.value = this.value;" /> 100,000 </td>
<td> <input type="radio" name="donation" value="75000.00" onClick="form.tamount.value = this.value;" /> 75,000 </td>
<td> <input type="radio" name="donation" value="50000.00" onClick="form.tamount.value = this.value;" /> 50,000 </td>
<td> <input type="radio" name="donation" id="twentyfive" value="25000.00" checked="checked" onClick="form.tamount.value = this.value;" /> 25,000 </td>
<td> <input type="radio" name="donation" value="Other" onClick="form.tamount.value = form.other.value;" /> Other</td>
<td> <input type="text" name="other" id="other" onBlur="form.tamount.value = this.value;checkother();" placeholder="Digits only" /></td></tr>
<tr id="repeating" style="display:none"><td><input type="radio" name="donation" value="50000.00" onClick="form.tamount.value = this.value;" /> 50,000 </td>
<td> <input type="radio" name="donation" value="40000.00" onClick="form.tamount.value = this.value;" /> 40,000 </td>
<td> <input type="radio" name="donation" value="20000.00" onClick="form.tamount.value = this.value;" /> 20,000 </td>
<td> <input type="radio" id="ten" name="donation" value="10000.00" onClick="form.tamount.value = this.value;" /> 10,000 </td>
<td><input type="radio"  name="donation" value="Other" onClick="form.tamount.value = form.Rother.value;" /> Other</td>
<td><input type="text" name="rother" id="rother" value="" onBlur="form.tamount.value = this.value;checkrother();" placeholder="Digits only"  /></td></tr>  
        <tr>
      <td><br /></td>
      <td colspan="5"></td>
    </tr>
    
     <tr>
      <td><input type="radio" name="regtype" value="Donate Later" onClick="hideblock(paymentmethod);this.form.action='donationmail.php';form.paynow.value = ' Donate Later ';" /></td>
      <td colspan="4">I would like to pay later, please contact me by email / phone</td><td>
      <input type="radio" name="regtype" value="Donate Now" checked="checked" onClick="showblock(paymentmethod);this.form.action='donatehdfc.php';form.paynow.value = ' Donate Later ';" /> I would like to pay now</td>
    </tr>
     <tr id="paymentmethod">
<td><input type="radio" value="hdfc" name="paymenttype" checked required onClick="this.form.action='donatehdfc.php'"  /></td>
<td> Via Credit Card</td>
<td><input name="paymenttype" type="radio" value="billdesk" required onClick="this.form.action='donatebilldesk.php'"></td>
<td colspan="3"> Via Bank Transfer (only for Banks within India)</td>
    </tr>
     <tr>
      <td colspan="2">Total Donation Amount</td>
      <td colspan="4"><input type="text" value="25000.00" name="tamount" />
      <input type="hidden" value="" name="remark" readonly width="353px" /></td>
      </tr>
    <tr>
   	<td colspan="6"><h3>Notes</h3></td>
    </tr>
       <tr>
   	<td colspan="6"><ul>
    <li>IIIT-Delhi urges all alumni to contribute to their alma mater, at least 1% of their yearly income to the Institute.</li>
    <li>IIITD is registered under section 80G of the Income Tax Act, 1961 that entitles a donor to claim 50% deduction on amount donated to Institute. Upon donation the Institute will issue a receipt mentioning amount donated, approval number, and date etc. for claiming deduction.</li></ul></td>
    </tr>
        
  <tr>
    <td colspan="6" align="center"><input name="MTrackid" size="25" value="90002954" type="hidden" />
    <input type="submit" name="paynow" value=" DONATE NOW " />
</td>
  </tr>
    </TBODY>
  </table>
</form>
    </div>


</div>

<div class="col-lg-3">
    


 

    


</div>

</div>

<div class="row">
    <div class="col-lg-offset-1 col-lg-10" id="green-dabba-2"></div>
</div>

<div class="row">
    <div class="footer">
        <div class="col-lg-4">
            <img src="http://alumni.iiitd.edu.in/static/alumniportal/img/Logo.png" width="300" />
        </div>
        <div class="col-lg-8">
            <ul>
                <li><a>Home</a></li>
                <li><span>|</span></li>
                <li><a>About Us</a></li>
                <li><span>|</span></li>
                <li id="openfeedback"><a>Feedback</a></li>
                <li><span>|</span></li>
                <li><a>Contact Us</a></li>
            </ul>
        </div>
    </div>
</div>

<div id="black"></div>



</div>
<script type="application/javascript">
function showblock(t){
	t.style.display='';
	}
function hideblock(t){
	t.style.display='none';
	}
function check()
	{
	var m = document.getElementById('mobile').value;
		if(isNaN(m))
		{
		alert (m + " is not a valid number");	
		}
	}
	function checkother()
	{
	var m = document.getElementById('other').value;
		if(isNaN(m))
		{
		alert (m + " is not a valid number");	
		}
	}
	function checkrother()
	{
	var m = document.getElementById('rother').value;
		if(isNaN(m))
		{
		alert (m + " is not a valid number");	
		}
	}
</script>
</body>

</html>