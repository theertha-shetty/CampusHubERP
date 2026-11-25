from app.api import create_app
from app.utils.database import create_all_tables


def main():
    create_all_tables()

    app = create_app()
    app.run(debug=True)


if __name__ == "__main__":
    main()