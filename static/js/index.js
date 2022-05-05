function sliderProject() {
    var swiper = new Swiper('.project-detail .swiper-container', {
        slidesPerView: 'auto',
        spaceBetween: 30,
        speed: 1100,
        loop: true,
        centeredSlides: true,
        navigation: {
            nextEl: '.project-detail .swiper-button-next',
            prevEl: '.project-detail .swiper-button-prev',
        },
        breakpoints: {
            220: {
                spaceBetween: 10
            },
            992: {
                spaceBetween: 30
            },

        }
    })
}


let orderType = $("input[name='order_type_m']:checked").val()

let quizFormData = {
    orderType: orderType,
    distanceToSea: '',
    budget: '',
    countBedrooms: '',
    profitAssessment: '',
    assessmentDistrict: '',
    assessmentDistanceToSea: '',
    rentalPeriod: '',
    name: '',
    phone: ''
}



$(document).ready(function() {
    //Валидация поля телефона на разные страны
    let isValidPhone = false
    $("input[name='phone']").keyup(function () {
        let inputValue = $(this).val()
        console.log(inputValue)
        console.log(inputValue.length)
        phoneValidation = inputValue
        if (inputValue.length > 8) { 
            if (inputValue.length < 13) {
                if (inputValue.charAt(0) == '+') {
                    isValidPhone = true;
                    $("[id=valid-phone]").text('')
                    $("[id=valid-phone]").addClass( "valid" );
                    $("[id=valid-phone]").removeClass( "novalid" );
                    console.log('Valide number')
                }
                else {
                    isValidPhone = false 
                    $("[id=valid-phone]").addClass( "novalid" );
                    $("[id=valid-phone]").removeClass( "valid" );
                    if (local == 'ru')
                        $("[id=valid-phone]").text('Укажите номер в международном формате.')
                    else
                        $("[id=valid-phone]").text('Please enter the number in international format.')
                }
            }
            else {
                isValidPhone = false
                $("[id=valid-phone]").addClass( "novalid" );
                $("[id=valid-phone]").removeClass( "valid" );
                if (local == 'ru')
                    $("[id=valid-phone]").text('Ваш номер телефона слишком большой.')
                else
                    $("[id=valid-phone]").text('Your phone number is too big.')
            }
        }
        else {
            isValidPhone = false
            if (inputValue.length == 0)
                $("[id=valid-phone]").text('')
            else {
                $("[id=valid-phone]").addClass( "novalid" );
                $("[id=valid-phone]").removeClass( "valid" );
                if (local == 'ru')
                    $("[id=valid-phone]").text('Ваш номер телефона слишком маленький.')
                else
                    $("[id=valid-phone]").text('Your phone number is too small.')
            }
            
        }
    })
    sliderProject()
        // $('input[type="tel"]').mask('+7 (999) 999-9999', { placeholder: '+7 (       )         -' });

    $(".projects__all").click(function() {
        $(".projects__item").removeClass("projects__item--hide")
        $(this).hide()
    })

    $(".qa__item-show").click(function() {
        if ($(this).hasClass("qa__item-show--active")) {
            $(".qa__item-show").removeClass("qa__item-show--active")
        } else {
            $(".qa__item-show").removeClass("qa__item-show--active")
            $(this).addClass("qa__item-show--active")
        }
    })

    $(".quiz__rating-item").click(function() {
        let ratingItem = parseInt($(this).attr("data-rating-value"))
        $(this).parent(".quiz__rating").attr("data-total-rating", ratingItem)
    })

    let yearRange = $("#yearRange")
    let rangeStart = yearRange.attr("min")
    let rangeEnd = yearRange.attr("max")
    let rangeCenter = (+rangeStart + +rangeEnd) / 2
    let rangeValue = yearRange.attr("value")
    $(".quiz__year-range-start span").text(rangeStart)
    $(".quiz__year-range-center span").text(rangeCenter)
    $(".quiz__year-range-end span").text(rangeEnd)
    $(".quiz__year-range-value span").text(rangeValue)

    $(".language-show").click(function() {
        $(this).addClass("language-show--active")
    })

    $(document).mouseup(function(e) { // событие клика по веб-документу
        var div = $(".language-hidden"); // тут указываем ID элемента
        if (!div.is(e.target) // если клик был не по нашему блоку
            &&
            div.has(e.target).length === 0) { // и не по его дочерним элементам
            if ($(".language-hidden").siblings(".language-show").hasClass("language-show--active")) {
                $(".language-hidden").siblings(".language-show").removeClass("language-show--active")
            }

        }
    });

    $(".header__burger").click(function() {
        $(this).toggleClass("header__burger--active")
        $(".header__right").slideToggle()
    })

    $(".quiz__finish-form-btn").click(function() {
        quizFormData.name = $("#quizName").val()
        quizFormData.phone = $("#quizPhone").val()
        console.log(quizFormData)
    })

    $(".quiz__step-consult").click(function() {
        $(`.quiz__step`).removeClass("quiz__step--active")
        $(`.quiz__step-last`).addClass("quiz__step--active")
    })

})





function nextStep(num, line) {
    if (num == 1) {
        let typeInput = $("input[name='order_type_m']:checked").val()
        console.log(typeInput)
        if (typeInput === 'R') {
            $(`.quiz__step`).removeClass("quiz__step--active")
            $(`.quiz__step[data-step-line='1'][data-step-path='2']`).addClass("quiz__step--active")
        } else if (typeInput === 'C') {
            $(`.quiz__step`).removeClass("quiz__step--active")
            $(`.quiz__step[data-step-line='2'][data-step-path='2']`).addClass("quiz__step--active")
        }
        quizFormData.orderType = typeInput
        console.log(quizFormData)
    }
    if (line == 1 && num == 2) {
        let ratingField = []
        $.each($('.quiz__rating'), function(i, el) {
            let ratingValue = $(el).attr("data-total-rating")
            if (ratingValue > 0) {
                ratingField.push(true)
            } else {
                ratingField.push(false)
            }
        });
        if (!ratingField.includes(false)) {
            $(`.quiz__step`).removeClass("quiz__step--active")
            $(`.quiz__step[data-step-line='1'][data-step-path='3']`).addClass("quiz__step--active")

            quizFormData.profitAssessment = +$("#profitAssessment").attr("data-total-rating")
            quizFormData.assessmentDistrict = +$("#assessmentDistrict").attr("data-total-rating")
            quizFormData.assessmentDistanceToSea = +$("#assessmentDistanceToSea").attr("data-total-rating")

        }
    }
    if (line == 2 && num == 2) {
        $(`.quiz__step`).removeClass("quiz__step--active")
        $(`.quiz__step[data-step-line='2'][data-step-path='3']`).addClass("quiz__step--active")

        quizFormData.distanceToSea = $("input[name='distance']:checked").val()

    }
    if (line == 2 && num == 3) {
        $(`.quiz__step`).removeClass("quiz__step--active")
        $(`.quiz__step[data-step-line='2'][data-step-path='4']`).addClass("quiz__step--active")

        quizFormData.rentalPeriod = $("#yearRange").val()

    }
    if (num == 100) {
        $(`.quiz__step`).removeClass("quiz__step--active")
        $(`.quiz__step-last`).addClass("quiz__step--active")

        if (line == 1) {
            quizFormData.budget = $("input[name='budget_m']:checked").val()
        }
        if (line == 2) {
            quizFormData.countBedrooms = $("input[name='area']:checked").val()
        }
    }
    if (num == 101) {
        $(`.quiz__step`).removeClass("quiz__step--active")
        $(`#thanks`).addClass("quiz__step--active")
        $('#thanks').css('display', 'block');
    }
}

function prevStep(num, line) {
    if (num == 2) {
        $(`.quiz__step`).removeClass("quiz__step--active")
        $(`.quiz__step-start`).addClass("quiz__step--active")
    }
    if (line == 1 && num == 3) {
        $(`.quiz__step`).removeClass("quiz__step--active")
        $(`.quiz__step[data-step-line='1'][data-step-path='2']`).addClass("quiz__step--active")
    }
    if (line == 2 && num == 3) {
        $(`.quiz__step`).removeClass("quiz__step--active")
        $(`.quiz__step[data-step-line='2'][data-step-path='2']`).addClass("quiz__step--active")
    }
    if (line == 2 && num == 4) {
        $(`.quiz__step`).removeClass("quiz__step--active")
        $(`.quiz__step[data-step-line='2'][data-step-path='3']`).addClass("quiz__step--active")
    }

}

function clickOutsideElemnt(div, e) {
    if (!div.is(e.target) &&
        div.has(e.target).length === 0) {
        div.hide();
    }
}


function range(el) {
    let range = $(el)
    let val = range.val();
    $(".quiz__year-range-value span").text(val)
}


function onIn() {
    if (window.innerWidth > 992) {
        let el = $(this)
        setTimeout(function() {
            if (el.is(':hover')) {
                el.children(".nav__item-hidden").addClass("nav__item-hidden--active")
            }

        }, 200);
    }
}

function onOut() {
    if (window.innerWidth > 992) {
        $(this).children(".nav__item-hidden").removeClass("nav__item-hidden--active")
    }
}


// let page_num = 1;

// // Фунция подгрузки реализованных проектов по 3 за раз.
// function sendRequestToGetProjects() {
//     let url_pattern = document.getElementById('url_pattern_for_paginate').value;
//     $.ajax({
//         url: url_pattern,
//         method: 'get',
//         dataType: 'html',
//         data: {'page_num': page_num},
//         success: function(data) {
//             parsed_data = JSON.parse(data);
            
//             for (let i = 0; i < parsed_data.length; i++) {
//                 let a = document.createElement('a');
//                 a.setAttribute('href', parsed_data[i].url);
//                 a.setAttribute('class', 'projects__item');

//                 let div_img = document.createElement('div');
//                 div_img.setAttribute('class', 'projects__item-img');
//                 let img = document.createElement('img');
//                 img.setAttribute('img', parsed_data[i].img_src);
//                 let more_info = document.createElement('div');
//                 more_info.setAttribute('class', 'projects__item-link');
//                 div_img.append(img);
//                 div_img.append(more_info);
//                 a.append(div_img);

//                 let proj_name = document.createElement('div');
//                 proj_name.setAttribute('class', 'projects__item-title');
//                 proj_name.innerHTML = parsed_data[i].name

//                 a.append(proj_name);

//                 document.getElementById('projects__items').append(a);
//             }
//             page_num++;
//         },
//         beforeSend: function() {

//         }
//     });
// }
