openerp.web_sba_debrand = function(instance) {
// меняем заголовок закладки в броузере	
	instance.web.WebClient.include({
	    init: function(parent, client_options) {
        this._super(parent, client_options);
        this.set('title_part', {"zopenerp": 'SBA'});
   //     console.log("000000000000");
    },
 });

	instance.web.CrashManager.include({
		// убираем Odoo из диалога ошибок
	    show_warning: function(error) {
        if (!this.active) {
            return;
        }
        if (error.data.exception_type === "except_osv") {
            error = _.extend({}, error, {data: _.extend({}, error.data, {message: error.data.arguments[0] + "\n\n" + error.data.arguments[1]})});
        }
        new instance.web.Dialog(this, {
            size: 'medium',
            title: "SbaErp " + (_.str.capitalize(error.type) || "Warning"),
            buttons: [
                {text: _t("Ok"), click: function() { this.parents('.modal').modal('hide'); }}
            ],
        }, $('<div>' + QWeb.render('CrashManager.warning', {error: error}) + '</div>')).open();
    },
    show_error: function(error) {
        if (!this.active) {
            return;
        }
        var buttons = {};
        buttons[_t("Ok")] = function() {
            this.parents('.modal').modal('hide');
        };
        new instance.web.Dialog(this, {
            title: "SbaErp " + _.str.capitalize(error.type),
            buttons: buttons
        }, QWeb.render('CrashManager.error', {session: instance.session, error: error})).open();
    },
    show_message: function(exception) {
        this.show_error({
            type: _t("Client Error"),
            message: exception,
            data: {debug: ""}
        });
    },
	});
};
/*
	instance.web.UserMenu.include({
// добавляем название БД в логине		
	    do_update: function () {
        var self = this;
        var fct = function() {
            var $avatar = self.$el.find('.oe_topbar_avatar');
            $avatar.attr('src', $avatar.data('default-src'));
            if (!self.session.uid)
                return;
            var func = new instance.web.Model("res.users").get_func("read");
            return self.alive(func(self.session.uid, ["name", "company_id"])).then(function(res) {
                var topbar_name = res.name;
                //if(instance.session.debug)
                    topbar_name = _.str.sprintf("%s (%s)", topbar_name, instance.session.db);
                if(res.company_id[0] > 1)
                    topbar_name = _.str.sprintf("%s (%s)", topbar_name, res.company_id[1]);
                self.$el.find('.oe_topbar_name').text(topbar_name);
                if (!instance.session.debug) {
                    topbar_name = _.str.sprintf("%s (%s)", topbar_name, instance.session.db);
                }
                var avatar_src = self.session.url('/web/binary/image', {model:'res.users', field: 'image_small', id: self.session.uid});
                $avatar.attr('src', avatar_src);

                openerp.web.bus.trigger('resize');  // Re-trigger the reflow logic
            });
        };
        this.update_promise = this.update_promise.then(fct, fct);
    },
 });
};
*/
/*
    do_update: function () {
        var self = this;
        var fct = function() {
            var $avatar = self.$el.find('.oe_topbar_avatar');
            $avatar.attr('src', $avatar.data('default-src'));
            if (!self.session.uid)
                return;
            var func = new instance.web.Model("res.users").get_func("read");
            return self.alive(func(self.session.uid, ["name", "company_id"])).then(function(res) {
                var topbar_name = res.name;
                if(instance.session.debug)
                    topbar_name = _.str.sprintf("%s (%s)", topbar_name, instance.session.db);
                if(res.company_id[0] > 1)
                    topbar_name = _.str.sprintf("%s (%s)", topbar_name, res.company_id[1]);
                self.$el.find('.oe_topbar_name').text(topbar_name);
                if (!instance.session.debug) {
                    topbar_name = _.str.sprintf("%s (%s)", topbar_name, instance.session.db);
                }
                var avatar_src = self.session.url('/web/binary/image', {model:'res.users', field: 'image_small', id: self.session.uid});
                $avatar.attr('src', avatar_src);

                openerp.web.bus.trigger('resize');  // Re-trigger the reflow logic
            });
        };
        this.update_promise = this.update_promise.then(fct, fct);
    },

*/