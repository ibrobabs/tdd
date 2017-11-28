// QUnit.test( "smoke test", function( assert ) {
        //     assert.equal($('.has-error').is(':visible'), true);
        //     $('.has-error').hide();
        //     assert.equal($('.has-error').is(':visible'), false);
        // });
        // QUnit.test( "smoke test 2", function( assert ) {
        //     assert.equal($('.has-error').is(':visible'), true);
        //     $('.has-error').hide();
        //     assert.equal($('.has-error').is(':visible'), false);
        // });

        $('input[name="text"]').on('keypress', function () {
            console.log('in keypress handler');
            $('.has-error').hide();
          });
          console.log('list.js loaded');