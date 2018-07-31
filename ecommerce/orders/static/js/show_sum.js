expand = true
function test_script(total, order_no){
	if (expand) {
        document.getElementsByTagName('button')[order_no-1].innerHTML = total
		expand = false
	} else {
	    document.getElementsByTagName('button')[order_no-1].innerHTML = "Show sum"
	    expand = true
	}
}