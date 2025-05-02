import flet as ft
import flet_permission_handler as fph
from notification import send_notification


def main(page: ft.Page):
    page.title = "🔔 Notification Application"
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.appbar = ft.AppBar(title=ft.Text("🔐 Notification Permission Manager"))

    ph = fph.PermissionHandler()
    page.overlay.append(ph)

    # Text element to display the status of notifications
    # status_text = ft.Text(
    #    "🔒 Notification permission status unknown...", color=ft.Colors.GREY
    # )

    # Notification button
    notify_button = ft.ElevatedButton("Send Notification", disabled=True)

    # Function to handle notification sending
    def on_notify_click(e):
        title = title_input.value
        text = message_input.value
        send_notification(
            title,
            text,
        )
        page.update()

    notify_button.on_click = on_notify_click

    # Function to check permission status
    def check_permission(e):
        result = ph.check_permission(e.control.data)
        print(f"Permission check: {e.control.data.name} - {result}")
        notify_button.disabled = not result
        page.update()

    # Function to request notification permission
    def request_permission(e):
        result = ph.request_permission(e.control.data)
        resultt = ph.request_permission(fph.PermissionType.ACCESS_NOTIFICATION_POLICY)
        print(f"Permission requested: {e.control.data.name} - {result}")
        notify_button.disabled = not result
        page.update()

    # Building the UI components
    title_input = ft.TextField(hint_text="Title")
    message_input = ft.TextField(hint_text="Message")
    page.add(
        ft.SafeArea(
            ft.Column(
                controls=[
                    title_input,
                    message_input,
                    ft.OutlinedButton(
                        "Check Notification Permission",
                        data=fph.PermissionType.NOTIFICATION,
                        on_click=check_permission,
                    ),
                    ft.OutlinedButton(
                        "Request Notification Permission",
                        data=fph.PermissionType.NOTIFICATION,
                        on_click=request_permission,
                    ),
                    notify_button,
                ]
            )
        )
    )


ft.app(main)
