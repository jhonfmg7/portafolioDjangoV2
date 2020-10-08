$(function() {
    'use strict';
    $('#btn_contact').prop('disabled', true)
    $('#name').on('input', () => {
        $('#btn_contact').prop('disabled', false)
        if ($('#name')[0].value === '' || $('#email')[0].value === '' || $('#message')[0].value === '') {
            $('#btn_contact').prop('disabled', true)
        }
    })
    $('#email').on('input', () => {
        $('#btn_contact').prop('disabled', false)
        if ($('#name')[0].value === '' || $('#email')[0].value === '' || $('#message')[0].value === '') {
            $('#btn_contact').prop('disabled', true)
        }
    })
    $('#message').on('input', () => {
        $('#btn_contact').prop('disabled', false)
        if ($('#name')[0].value === '' || $('#email')[0].value === '' || $('#message')[0].value === '') {
            $('#btn_contact').prop('disabled', true)
        }
    })
})