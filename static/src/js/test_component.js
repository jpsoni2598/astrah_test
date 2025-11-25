/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

export class PingConsoleComponent extends Component {
    static template = "astrah_test.PingConsoleComponent";

    // function to ping the console
    pingConsole() {
        console.log("Astrah Test Component button clicked");
    }
}

registry.category("view_widgets").add("astrah_test_ping_console", {
    component: PingConsoleComponent
});