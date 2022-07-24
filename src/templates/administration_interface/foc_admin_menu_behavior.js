let left_side = document.querySelector("div#left-split");
let left_blank = document.querySelector("div#left-blank");
let left_button = document.querySelector("button#left-button");
let left_sub_buttons = document.querySelector("div#left-sub-buttons");
let left_back_button = document.querySelector("button#left-back-button");

let right_side = document.querySelector("div#right-split");
let right_blank = document.querySelector("div#right-blank");
let right_button = document.querySelector("button#right-button");
let right_sub_buttons = document.querySelector("div#right-sub-buttons");
let right_back_button = document.querySelector("button#right-back-button");

let animation_state = 0;
let button_showing = 0;
let right_button_showing = 0;

left_button.addEventListener("click", leftClicked);
left_back_button.addEventListener("click", leftBackClicked);
left_back_button.addEventListener("animationend", leftBackOff);

right_button.addEventListener("click", rightClicked);
right_back_button.addEventListener("click", rightBackClicked);
right_back_button.addEventListener("animationend", rightBackOff);

left_blank.addEventListener("animationend", resetLayoutRight);
right_blank.addEventListener("animationend", resetLayoutLeft);



function leftClicked() {
	console.log("left was clicked!");
	left_side.className = "split-grow";
	right_blank.className = "split-shrink";
	animation_state = 1;
}

function leftBackClicked() {
	console.log("left back button was clicked!");

	left_back_button.className = "back-button-hide";
	left_sub_buttons.className = "button-row-hide";
	left_button.className = "title-to-button";

	button_showing = 0;

}

function rightClicked() {
	console.log("right was clicked!");
	right_side.className = "split-grow";
	left_blank.className = "split-shrink";
	animation_state = 1;
}

function rightBackClicked() {
	console.log("right back button was clicked!");
	right_back_button.className = "back-button-hide";
	right_sub_buttons.className = "button-row-hide";

	right_button.className = "title-to-button";
	button_showing = 0;
}

function resetLayoutLeft() {
	console.log("layout resetting after LEFT animation...");
	if ( animation_state == 1 ) { 
		left_back_button.className = "back-button-show";
		left_sub_buttons.className = "button-row-show";
		left_button.className = "button-to-title";

		button_showing = 1;
		left_side.className = "split-big";
		right_blank.className = "split-small";
	} else {
		left_side.className = "split";
		right_blank.className = "split";
	}
}

function resetLayoutRight() {
	console.log("layout resetting after RIGHT animation...");
	if ( animation_state == 1 ) { 
		right_back_button.className = "back-button-show";
		right_sub_buttons.className = "button-row-show";
		right_button.className = "button-to-title";

		button_showing = 1;
		right_side.className = "split-big";
		left_blank.className = "split-small";
	} else {

		right_side.className = "split";
		left_blank.className = "split";
	}
}

function leftBackOff() { console.log("TRYING to turn off left back button");

	if ( button_showing == 0 ) {console.log("turning off left back button");
		left_back_button.className = "back-button";

		left_side.className = "split-un-grow";
		right_blank.className = "split-un-shrink";

		animation_state = 0;
	}
}

function rightBackOff() { console.log("turning off RIGHT back button");
	if ( button_showing == 0 ) {
		right_back_button.className = "back-button";

		right_side.className = "split-un-grow";
		left_blank.className = "split-un-shrink";

		animation_state = 0;
	}
}