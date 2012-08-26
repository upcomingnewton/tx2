// JavaScript Document
function checkmail(check_ob)
{
	var elem_id = check_ob.type;
	var val=document.getElementById(elem_id);

	if(txValidateEmail(val) == true){
		if(txValidateMaxLength(val, parseInt(check_ob.max_)) == true){
			return true;
		}
		else{
			val.value='';
			val.placeholder='Too long, Not a Valid Email Address..!';
			return false;
		}
		
	}
	else if(txValidateEmpty(val)==true)
	{
		val.value='';
		val.placeholder='Email Address Please..!';
		return false;
	}
	else
	{
		val.value='';
		val.placeholder='Valid Email Address Please..!';
		return false;
	}
}

function checkname(check_ob,error_id)
{
	var elem_id = check_ob.type;
	var val=document.getElementById(elem_id);

	
	if(txValidateAlphabet(val) == true){
		if(txValidateMinLength(val, parseInt(check_ob.min_)) == true){
			return true;
		}
		else{
			val.value='';
			val.placeholder='Name Too Short..!';
			return false;
		}
		
	}
	else if(txValidateEmpty(val)==true)
	{
		if(elem_id == 'mname'){
			return true;
		}
		else{
			val.value='';		
			val.placeholder='Name Please..!';
			return false;
		}
	}
	else
	{
		val.value='';
		val.placeholder='Valid Name Please..!';
		return false;
	}
}

function checkpass(check_ob)
{
	var elem_id = check_ob.type;
	var val=document.getElementById(elem_id);

	
	if(txValidateEmpty(val)==true)
	{
		val.value='';
		val.placeholder='Please Enter Password..!';
		return false;
	}
	else
	{
		if(txValidateMinLength(val, parseInt(check_ob.min_)) == true){
			return true;
			}
		else{
			val.value='';
			val.placeholder='Password too short..!';
			return false;
		}
	}

}
function checkpass2(check_ob){
	var elem_id = check_ob.type;
	var checkpass_id = check_ob.chkfrom;
	var val=document.getElementById(elem_id);
	var val_chk=document.getElementById(checkpass_id);
	if(val.value == val_chk.value){
		return true;
	}
	else{
		val.value='';
		val.placeholder='Passwords do not match..!';
		return false;
	}
}

function checkdate(elem_id){
	var date = document.getElementById(elem_id).value;
	var val = document.getElementById(elem_id);
	if(txValidateDate(date) == true){
		return true;
	}
	else{
		val.value='';
		val.placeholder='Date invalid..! Please enter your Date Of Birth as mm/dd/yyyy';
		return false;
	}
}
//All of the generic functions here:
function txValidateEmail(val)
{
	var chk_exp= /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/;
	
	if(val.value.match(chk_exp))
	{
		return true;
	}
	else
	{
		return false;
	}
}
function txValidateMinLength(val,i)
{
	if(val.value.length > i)
	{
		return true;
	}
	else
	{
		return false;
	}
}

function txValidateMaxLength(val,i)
{
	if(val.value.length < i)
	{
		return true;
	}
	else
	{
		return false;
	}
}
function txValidateEmpty(val)
{
	if(val.value.length == 0){
		return true;
	}
	else{
		return false;
	}
}
function txValidateNumber(val)
{
	var chk_exp =  /^[0-9]+$/;
	if(val.value.match(chk_exp))
	{
		return true;
	}
	else
	{
		return false;
	}
}
function txValidateAlphabet(val)
{
	var chk_exp= /^[a-zA-Z]+$/;
	if(val.value.match(chk_exp))
	{
		return true;
	}
	else
	{
		return false;
	}
}
function txValidateAlphaNumeric(val)
{
	var chk_exp=/^[0-9a-zA-Z]+$/;
	if(val.value.match(chk_exp))
	{
		return true;
	}
	else
	{
		return false;
	}
}
function txValidateName(val){
	var chk_exp=/^[/ a-zA-Z]+$/;
	if(val.value.match(chk_exp))
	{
		return true;
	}
	else
	{
		return false;
	}
}
function txValidateDate(txtDate) {
    var objDate,  // date object initialized from the txtDate string
        mSeconds, // txtDate in milliseconds
        day,      // day
        month,    // month
        year;     // year
    // date length should be 10 characters (no more no less)
    if (txtDate.length !== 10) {
        return false;
    }
    // third and sixth character should be '/'
    if (txtDate.substring(2, 3) !== '/' || txtDate.substring(5, 6) !== '/') {
        return false;
    }
    // extract month, day and year from the txtDate (expected format is mm/dd/yyyy)
    // subtraction will cast variables to integer implicitly (needed
    // for !== comparing)
    month = txtDate.substring(0, 2) - 1; // because months in JS start from 0
    day = txtDate.substring(3, 5) - 0;
    year = txtDate.substring(6, 10) - 0;
    // test year range
    if (year < 1000 || year > 3000) {
        return false;
    }
    // convert txtDate to milliseconds
    mSeconds = (new Date(year, month, day)).getTime();
    // initialize Date() object from calculated milliseconds
    objDate = new Date();
    objDate.setTime(mSeconds);
    // compare input date and parts from Date() object
    // if difference exists then date isn't valid
    if (objDate.getFullYear() !== year ||
        objDate.getMonth() !== month ||
        objDate.getDate() !== day) {
        return false;
    }
    // otherwise return true
    return true;
}