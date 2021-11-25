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
            // 320: {
            //     slidesPerView: 1,
            //     spaceBetween: 0
            // },
            // 480: {
            //     slidesPerView: 1,
            //     spaceBetween: 0
            // },

        }
    })
}




$(document).ready(function() {
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

    $(".header__language-show").click(function() {
        $(this).addClass("header__language-show--active")
    })

    $(document).mouseup(function(e) { // событие клика по веб-документу
        var div = $(".header__language-hidden"); // тут указываем ID элемента
        if (!div.is(e.target) // если клик был не по нашему блоку
            &&
            div.has(e.target).length === 0) { // и не по его дочерним элементам
            if ($(".header__language-hidden").siblings(".header__language-show").hasClass("header__language-show--active")) {
                $(".header__language-hidden").siblings(".header__language-show").removeClass("header__language-show--active")
            }

        }
    });

})

function nextStep(num, line) {
    if (num == 1) {
        let typeInput = $("input[name='type']:checked").val()
        console.log(typeInput)
        if (typeInput === 'rent') {
            $(`.quiz__step`).removeClass("quiz__step--active")
            $(`.quiz__step[data-step-line='1'][data-step-path='2']`).addClass("quiz__step--active")
        } else if (typeInput === 'construct') {
            $(`.quiz__step`).removeClass("quiz__step--active")
            $(`.quiz__step[data-step-line='2'][data-step-path='2']`).addClass("quiz__step--active")
        }
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
        }
    }
    if (line == 2 && num == 2) {
        $(`.quiz__step`).removeClass("quiz__step--active")
        $(`.quiz__step[data-step-line='2'][data-step-path='3']`).addClass("quiz__step--active")
    }
    if (line == 2 && num == 3) {
        $(`.quiz__step`).removeClass("quiz__step--active")
        $(`.quiz__step[data-step-line='2'][data-step-path='4']`).addClass("quiz__step--active")
    }
    if (line == 100) {
        $(`.quiz__step`).removeClass("quiz__step--active")
        $(`.quiz__step-last`).addClass("quiz__step--active")
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